# Deploy

Deployment assets for running Huginn as **one OpenClaw instance**. Deployment is an
implementation concern kept separate from the methodology
([ADR 0009](../docs/adr/0009-single-openclaw-instance-topology.md)).

| File | Purpose |
|---|---|
| [`install-openclaw-config.sh`](install-openclaw-config.sh) | Clear down an existing OpenClaw config and install Huginn (Linux/Ubuntu). **Runnable.** |
| [`openclaw.config.example.json5`](openclaw.config.example.json5) | Illustrative, annotated mapping of agents → skills. **Reference only** (contains extra explanatory keys OpenClaw would not accept). |

The installer generates the **real, valid** `openclaw.json`; the example file is for reading.

## `install-openclaw-config.sh`

Written in Bash for a Linux (Ubuntu) OpenClaw host. It follows the OpenClaw config model
(<https://docs.openclaw.ai/gateway/configuration>): config at `~/.openclaw/openclaw.json`
(JSON5), agents under `agents.entries.*`, skills discovered from `<workspace>/skills`.

### What it does (default = non-destructive reconcile)

1. **Verify** the Huginn repo sources exist (fails before touching anything).
2. **Back up** the entire existing `~/.openclaw` to a timestamped `~/.openclaw.backup-<ts>.tar.gz`
   (unless `--no-backup`).
3. **Install/reconcile**:
   - a shared workspace `~/.openclaw/workspace-huginn/` containing the Product Knowledge
     (`schemas/`, `templates/`, `governance/`, `docs/`, `agents/`, `canvases/`, `examples/`) and
     the `skills/` packages, plus an empty `records/` dir for live Product Knowledge;
   - a fresh `~/.openclaw/openclaw.json` mapping the **eight** Huginn agents to `agents.entries.*`
     (Product Owner is `default: true`), each attached to its skills, all sharing the one
     workspace so they share canonical Product Knowledge.
4. **Validate** with `openclaw config validate` / `openclaw doctor --fix` if the CLI is present.

> ⚠️ **Optional destructive mode.** Use `--full-reset` to delete everything under `~/.openclaw`.
> In full-reset mode, the script requires you to type `reset` to confirm (unless `--yes`) and
> always backs up first unless you pass `--no-backup`. On failure after backup, it attempts an
> automatic rollback from the backup. Manual restore command:
> `rm -rf ~/.openclaw && tar -xzf ~/.openclaw.backup-<ts>.tar.gz -C ~`

### Usage

On the Ubuntu host, from a checkout of this repo:

```bash
# Preview everything, change nothing:
./deploy/install-openclaw-config.sh --dry-run

# Do it (prompts for confirmation, backs up first):
./deploy/install-openclaw-config.sh

# Full destructive reset + reinstall:
./deploy/install-openclaw-config.sh --full-reset

# Non-interactive (e.g. CI/provisioning):
./deploy/install-openclaw-config.sh --yes
```

### Options

| Option | Effect |
|---|---|
| `-y, --yes` | Skip confirmation prompts (required for non-interactive runs, including `--full-reset`). |
| `--dry-run` | Print planned actions and the generated config; change nothing. |
| `--full-reset` | Destructively remove `<openclaw-home>` before reinstalling everything. |
| `--no-backup` | Skip the safety backup (not recommended). |
| `--repo PATH` | Huginn repo location (default: the parent of the script). |
| `--openclaw-home P` | Override the state dir (default: `~/.openclaw`). |
| `--config-path P` | Override the config file (default: `$OPENCLAW_CONFIG_PATH` or `<home>/openclaw.json`). |
| `--workspace P` | Override the workspace dir (default: `<home>/workspace-huginn`). |

### After install

```bash
openclaw config get agents.entries        # confirm the eight agents
openclaw config validate                  # if not already run by the installer
# Validate Product Knowledge (needs python3 on the host):
pip3 install -r scripts/requirements.txt && python3 scripts/validate.py \
  ~/.openclaw/workspace-huginn/examples
```

### Notes & assumptions

- **Shared workspace.** All agents point at one workspace so Product Knowledge is shared (the core
  methodology principle). If your OpenClaw version prefers per-agent workspaces, adjust the
  generated `openclaw.json` or pass `--workspace` and re-run.
- **`human` is not an agent.** It is the reserved authority for `change_challenge` and
  `decide_pivot_reframe`; there is no `agents.entries.human`.
- **Per-agent skills** mirror each agent's charter; the full set is enabled in
  `agents.defaults.skills` and narrowed per agent.
