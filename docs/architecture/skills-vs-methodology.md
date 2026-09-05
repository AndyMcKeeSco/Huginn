# Skills vs Methodologies

Huginn keeps a firm line between a **skill** (a reusable capability, packaged as an OpenClaw
`SKILL.md`) and a **methodology** (a way of performing that capability well). **Methodologies live
inside skills.** They are never agents (see
[ADR 0010](../adr/0010-agents-as-responsibility-boundaries.md)).

## Definitions

- **Skill** — a reusable unit of capability with a stable contract: purpose, when to use, when not
  to use, inputs, Definition of Ready, methodology selection, process, structured output, quality
  criteria, Definition of Done, failure modes, escalation/governance. Lives in `skills/<name>/`.
- **Methodology** — a discipline a skill may apply: Continuous Discovery, Opportunity Solution
  Trees, JTBD, Impact Mapping, Lean Product/UX, Assumption Mapping, Riskiest Assumption Testing,
  Bayesian Updating, Weight of Evidence, Truth Maintenance, ResearchOps, Critical Appraisal,
  Evidence-Based Practice, Triangulation, Expected Value of Information, Design of Experiments,
  Build–Measure–Learn, Innovation Accounting, Pivot/Persevere, …

## The rule: one skill, many methodologies, selected in context

A skill's **"methodology selection"** section chooses the appropriate methodology for the
situation and records *why*. For example:

- `risk-assessment` may select riskiest-assumption thinking, EVI, decision analysis or WSJF — and
  never hard-codes one formula.
- `belief-revision` applies Bayesian updating / weight of evidence + truth maintenance.
- `evidence-appraisal` applies critical appraisal + adapted GRADE.

## Why this matters

- **Reuse.** The same methodology can appear in several skills without duplication.
- **Governance.** Because methods sit inside skills, agents stay defined by responsibility, and
  decision rights remain clean.
- **Evolvability.** A skill can adopt a better methodology later without changing agents or the
  reasoning kernel.

## The OpenClaw skill package

Each skill is a directory with a `SKILL.md` (YAML frontmatter `name` + `description`, then the
body) per <https://docs.openclaw.ai/tools/skills>, optionally with supporting `reference.md` and
using `{baseDir}` to refer to its own folder. Skills are attached to agents in
`deploy/openclaw.config.example.json5`.
