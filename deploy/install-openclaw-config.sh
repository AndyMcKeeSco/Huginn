#!/usr/bin/env bash
#
# install-openclaw-config.sh — clear down an existing OpenClaw configuration and install
# the Huginn single-instance configuration on a Linux (Ubuntu) host.
#
# DEFAULT BEHAVIOUR IS A NON-DESTRUCTIVE RECONCILE:
#   1. Verify the Huginn repo sources exist (fail early, before touching anything).
#   2. Back up the existing ~/.openclaw to a timestamped tar.gz (unless --no-backup).
#   3. Reconcile the managed Huginn workspace content and write a fresh openclaw.json.
#   4. Validate with `openclaw config validate` / `openclaw doctor` if the CLI is present.
#
# OPTIONAL: --full-reset performs a destructive reset of the OpenClaw state directory:
#   - Remove ~/.openclaw entirely (agents, workspaces, credentials, history — all of it).
#   - Recreate it from scratch before writing config/workspace content.
#
# --full-reset requires an interactive confirmation unless --yes is given, and backup is strongly
# recommended. On failure after backup, the script attempts automatic rollback from the backup.
#
# OpenClaw config model (https://docs.openclaw.ai/gateway/configuration):
#   * config file: ~/.openclaw/openclaw.json (JSON5), overridable via OPENCLAW_CONFIG_PATH
#   * agents under agents.entries.*, cross-agent defaults under agents.defaults
#   * skills enabled via agents.defaults.skills / agents.entries.*.skills, discovered from
#     <workspace>/skills
#
# Usage:
#   ./deploy/install-openclaw-config.sh [options]
#
# Options:
#   -y, --yes              Do not prompt for confirmation (required for non-interactive runs).
#       --dry-run          Print what would happen; change nothing.
#       --full-reset       Destructively remove <openclaw-home> before reinstalling.
#       --no-backup        Skip the safety backup of the existing ~/.openclaw (NOT recommended).
#       --repo PATH        Path to the Huginn repo (default: the parent of this script).
#       --openclaw-home P  Override the OpenClaw state dir (default: ~/.openclaw).
#       --config-path P    Override the config file path (default: <openclaw-home>/openclaw.json
#                          or $OPENCLAW_CONFIG_PATH if set).
#       --workspace P      Override the Huginn workspace dir (default:
#                          <openclaw-home>/workspace-huginn).
#   -h, --help             Show this help.
#
set -euo pipefail

# ---------------------------------------------------------------------------- helpers -------
log()  { printf '  %s\n' "$*"; }
info() { printf '\033[1m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[33mWARN:\033[0m %s\n' "$*" >&2; }
die()  { printf '\033[31mERROR:\033[0m %s\n' "$*" >&2; exit 1; }

DRY_RUN=0
run() { # execute unless dry-run
  if [ "$DRY_RUN" -eq 1 ]; then printf '  [dry-run] %s\n' "$*"; else eval "$@"; fi
}

# ---------------------------------------------------------------------------- defaults ------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OPENCLAW_HOME="${OPENCLAW_HOME:-$HOME/.openclaw}"
CONFIG_PATH="${OPENCLAW_CONFIG_PATH:-}"
WORKSPACE=""
ASSUME_YES=0
DO_BACKUP=1
FULL_RESET=0
BACKUP_CREATED=0
ROLLBACK_ENABLED=0

require_abs_path() {
  case "${1:-}" in
    "") die "$2 must not be empty" ;;
    /*) ;;
    *) die "$2 must be an absolute path: $1" ;;
  esac
}

guard_dangerous_dir() {
  case "$1" in
    "/"|"/."|"//") die "refusing unsafe path for $2: $1" ;;
  esac
}

guard_dangerous_file() {
  case "$1" in
    "/"|"/."|"//") die "refusing unsafe file path for $2: $1" ;;
  esac
}

attempt_rollback() {
  [ "$DRY_RUN" -eq 1 ] && return 0
  [ "$ROLLBACK_ENABLED" -eq 1 ] || return 0
  [ "$BACKUP_CREATED" -eq 1 ] || return 0
  [ -f "$BACKUP_TGZ" ] || return 0

  warn "install failed; attempting rollback from backup: $BACKUP_TGZ"
  set +e
  rm -rf "$OPENCLAW_HOME"
  mkdir -p "$(dirname "$OPENCLAW_HOME")"
  tar -xzf "$BACKUP_TGZ" -C "$(dirname "$OPENCLAW_HOME")"
  if [ $? -eq 0 ]; then
    warn "rollback completed"
  else
    warn "rollback failed; restore manually with: rm -rf '$OPENCLAW_HOME' && tar -xzf '$BACKUP_TGZ' -C '$(dirname "$OPENCLAW_HOME")'"
  fi
}

# ---------------------------------------------------------------------------- args ----------
while [ $# -gt 0 ]; do
  case "$1" in
    -y|--yes)        ASSUME_YES=1 ;;
    --dry-run)       DRY_RUN=1 ;;
    --full-reset)    FULL_RESET=1 ;;
    --no-backup)     DO_BACKUP=0 ;;
    --repo)          REPO_ROOT="$(cd "$2" && pwd)"; shift ;;
    --openclaw-home) OPENCLAW_HOME="$2"; shift ;;
    --config-path)   CONFIG_PATH="$2"; shift ;;
    --workspace)     WORKSPACE="$2"; shift ;;
    -h|--help)       sed -n '2,40p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)               die "unknown option: $1 (try --help)" ;;
  esac
  shift
done

[ -n "$CONFIG_PATH" ] || CONFIG_PATH="$OPENCLAW_HOME/openclaw.json"
[ -n "$WORKSPACE" ]   || WORKSPACE="$OPENCLAW_HOME/workspace-huginn"
TS="$(date +%Y%m%d-%H%M%S)"
BACKUP_TGZ="$OPENCLAW_HOME.backup-$TS.tar.gz"

require_abs_path "$OPENCLAW_HOME" "openclaw home"
require_abs_path "$CONFIG_PATH" "config path"
require_abs_path "$WORKSPACE" "workspace path"
guard_dangerous_dir "$OPENCLAW_HOME" "openclaw home"
guard_dangerous_file "$CONFIG_PATH" "config path"
guard_dangerous_dir "$WORKSPACE" "workspace"
[ "$OPENCLAW_HOME" != "$HOME" ] || die "refusing to operate on HOME directly: $OPENCLAW_HOME"
[ "$WORKSPACE" != "$OPENCLAW_HOME" ] || die "workspace must not equal openclaw home: $WORKSPACE"
if [ -L "$OPENCLAW_HOME" ]; then
  die "openclaw home must not be a symlink: $OPENCLAW_HOME"
fi
if [ -d "$CONFIG_PATH" ]; then
  die "config path must be a file path, not a directory: $CONFIG_PATH"
fi

# The Huginn directories copied into the workspace so all agents share Product Knowledge.
MANAGED_DIRS="skills schemas templates governance docs agents canvases examples"

# ------------------------------------------------------------ 1. verify repo sources --------
info "Huginn -> OpenClaw installer"
log "repo:           $REPO_ROOT"
log "openclaw home:  $OPENCLAW_HOME"
log "config file:    $CONFIG_PATH"
log "workspace:      $WORKSPACE"
log "mode:           $([ "$FULL_RESET" -eq 1 ] && echo "FULL RESET" || echo "RECONCILE (non-destructive)")"
[ "$DRY_RUN" -eq 1 ] && log "mode:           DRY RUN (no changes)"

[ -f "$REPO_ROOT/AGENTS.md" ] || die "does not look like the Huginn repo (no AGENTS.md): $REPO_ROOT"
for d in $MANAGED_DIRS; do
  [ -d "$REPO_ROOT/$d" ] || die "missing repo directory: $REPO_ROOT/$d"
done
[ -d "$REPO_ROOT/skills" ] || die "no skills to install"

# Build the skills list from the repo (any directory containing a SKILL.md).
ALL_SKILLS="$(cd "$REPO_ROOT/skills" && for s in */; do [ -f "${s}SKILL.md" ] && printf '%s\n' "${s%/}"; done | sort)"
[ -n "$ALL_SKILLS" ] || die "found no SKILL.md packages under $REPO_ROOT/skills"
SKILL_COUNT="$(printf '%s\n' "$ALL_SKILLS" | wc -l | tr -d ' ')"
log "skills found:   $SKILL_COUNT"

# ------------------------------------------------------------ 2. confirm --------------------
if [ "$FULL_RESET" -eq 1 ] && [ "$ASSUME_YES" -ne 1 ] && [ "$DRY_RUN" -ne 1 ]; then
  if [ ! -t 0 ]; then die "refusing to do a full reset non-interactively; pass --yes to proceed"; fi
  printf '\033[31mThis will DELETE the entire %s (all agents, workspaces, credentials, history)\033[0m\n' "$OPENCLAW_HOME"
  [ "$DO_BACKUP" -eq 1 ] && printf 'A backup will be written to %s first.\n' "$BACKUP_TGZ" || printf '\033[31mNO BACKUP will be taken (--no-backup).\033[0m\n'
  printf "Type 'reset' to continue: "
  read -r reply
  [ "$reply" = "reset" ] || die "aborted."
fi

# ------------------------------------------------------------ 3. backup ---------------------
if [ -d "$OPENCLAW_HOME" ]; then
  if [ "$DO_BACKUP" -eq 1 ]; then
    info "Backing up existing $OPENCLAW_HOME"
    run "tar -czf '$BACKUP_TGZ' -C '$(dirname "$OPENCLAW_HOME")' '$(basename "$OPENCLAW_HOME")'"
    [ "$DRY_RUN" -eq 1 ] || BACKUP_CREATED=1
    [ "$DRY_RUN" -eq 1 ] || ROLLBACK_ENABLED=1
    log "backup: $BACKUP_TGZ"
  else
    warn "skipping backup (--no-backup)"
  fi
else
  log "no existing $OPENCLAW_HOME to back up"
fi

# Best-effort: stop a running gateway so it does not rewrite the config from under us.
if [ "$FULL_RESET" -eq 1 ] && command -v openclaw >/dev/null 2>&1; then
  info "Stopping OpenClaw gateway (best effort)"
  run "openclaw gateway stop >/dev/null 2>&1 || true"
fi

# ------------------------------------------------------------ 4. clear down (full reset) ----
if [ "$FULL_RESET" -eq 1 ] && [ -d "$OPENCLAW_HOME" ]; then
  info "Removing $OPENCLAW_HOME (full reset)"
  run "rm -rf '$OPENCLAW_HOME'"
fi

# ------------------------------------------------------------ 5. install --------------------
trap 'attempt_rollback' ERR

info "Ensuring state dir and Huginn workspace"
run "mkdir -p '$OPENCLAW_HOME'"
run "mkdir -p '$WORKSPACE'"

info "Copying Huginn Product Knowledge + skills into the workspace"
for d in $MANAGED_DIRS; do
  log "-> $d/"
  run "rm -rf '$WORKSPACE/$d'"
  run "cp -R '$REPO_ROOT/$d' '$WORKSPACE/$d'"
done
# A place for live records; keep the worked example available as a seed under examples/.
run "mkdir -p '$WORKSPACE/records'"

# ------------------------------------------------------------ 6. write openclaw.json --------
info "Writing $CONFIG_PATH"
run "mkdir -p '$(dirname "$CONFIG_PATH")'"

# Per-agent skill attachments (must be a subset of ALL_SKILLS; mirrors deploy/openclaw.config.example.json5).
skills_json() { # $1..$n -> JSON array of quoted skill names
  printf '['; local first=1; for s in "$@"; do [ $first -eq 1 ] && first=0 || printf ', '; printf '"%s"' "$s"; done; printf ']'
}
DEFAULTS_SKILLS="$(skills_json $ALL_SKILLS)"
PO_SKILLS="$(skills_json intent-definition intent-alignment opportunity-assessment opportunity-selection opportunity-mapping risk-assessment learning-accounting pivot-persevere-assessment)"
DESIGNER_SKILLS="$(skills_json user-research test-design)"
ENGINEER_SKILLS="$(skills_json technical-investigation test-design)"
PROP_SKILLS="$(skills_json proposition-formation proposition-classification proposition-linking belief-revision contradiction-detection assumption-mapping)"
RO_SKILLS="$(skills_json test-design test-readiness knowledge-research data-analytics user-research technical-investigation)"
LS_SKILLS="$(skills_json evidence-appraisal learning-synthesis learning-validation)"
SCOUT_SKILLS="$(skills_json opportunity-discovery knowledge-research contradiction-detection)"
ACOS_SKILLS="$(skills_json risk-assessment canvas-management)"

TMP_CFG="$(mktemp)"
cat > "$TMP_CFG" <<JSON5
// Huginn — OpenClaw configuration (generated by deploy/install-openclaw-config.sh)
// Generated: $TS
// Single OpenClaw instance topology; see deploy/README.md and
// docs/adr/0009-single-openclaw-instance-topology.md. Deployment is separate from methodology.
{
  // Cross-agent defaults. All eight agents share ONE workspace so they share canonical
  // Product Knowledge (schemas/, records/, governance/) — the core methodology principle.
  agents: {
    defaults: {
      workspace: "$WORKSPACE",
      skills: $DEFAULTS_SKILLS,
    },
    entries: {
      "product-owner":         { default: true, workspace: "$WORKSPACE", skills: $PO_SKILLS },
      "designer":              { workspace: "$WORKSPACE", skills: $DESIGNER_SKILLS },
      "engineer":              { workspace: "$WORKSPACE", skills: $ENGINEER_SKILLS },
      "proposition-steward":   { workspace: "$WORKSPACE", skills: $PROP_SKILLS },
      "research-orchestrator": { workspace: "$WORKSPACE", skills: $RO_SKILLS },
      "learning-steward":      { workspace: "$WORKSPACE", skills: $LS_SKILLS },
      "product-scout":         { workspace: "$WORKSPACE", skills: $SCOUT_SKILLS },
      "ai-chief-of-staff":     { workspace: "$WORKSPACE", skills: $ACOS_SKILLS },
    },
  },
}
JSON5

if [ "$DRY_RUN" -eq 1 ]; then
  printf '  [dry-run] would write the following config:\n\n'
  sed 's/^/    /' "$TMP_CFG"
  rm -f "$TMP_CFG"
else
  # Atomic replace (OpenClaw expects the config path to be a regular file).
  mv "$TMP_CFG" "$CONFIG_PATH"
  log "wrote $CONFIG_PATH"
fi

# ------------------------------------------------------------ 7. validate -------------------
if command -v openclaw >/dev/null 2>&1; then
  info "Validating with the OpenClaw CLI"
  run "openclaw config validate || openclaw doctor --fix || true"
else
  warn "the 'openclaw' CLI was not found on PATH; skipping validation"
  warn "install/point OpenClaw at this config, then run: openclaw config validate"
fi

info "Done."
[ "$DRY_RUN" -eq 1 ] && exit 0
echo
echo "Next steps:"
echo "  1. Start (or let the Gateway hot-reload) OpenClaw; it watches $CONFIG_PATH."
echo "  2. Confirm the agents:      openclaw config get agents.entries"
echo "  3. Validate Product Knowledge (needs python3 + pip deps on this host):"
echo "         pip3 install -r $REPO_ROOT/scripts/requirements.txt"
echo "         python3 $REPO_ROOT/scripts/validate.py $WORKSPACE/examples"
if [ -f "$BACKUP_TGZ" ]; then
  echo "  4. Previous state backed up at: $BACKUP_TGZ"
  echo "     (restore with:  rm -rf '$OPENCLAW_HOME' && tar -xzf '$BACKUP_TGZ' -C '$(dirname "$OPENCLAW_HOME")')"
fi
