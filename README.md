# Huginn

An agentic product development process and harness.

Huginn is a **continuous, evidence-based product-development operating system** in which a
Product Trio works in shared sprints to reduce the most consequential risks to achieving an
intended outcome, using **the least costly sufficiently reliable way to learn**.

It draws on Teresa Torres (Continuous Discovery, Opportunity Solution Trees, Product Trios),
Jeff Gothelf (outcomes over outputs, hypotheses and assumptions, Lean UX) and Eric Ries
(Build–Measure–Learn, Validated Learning, Innovation Accounting, Pivot/Persevere), and adds an
explicit **machine-operable model** of intent, opportunities, propositions, tests, evidence,
learning, belief revision, risk, decisions, product knowledge, agent decision rights and human
governance.

> **v1 purpose.** Make Huginn's core **reasoning, research, learning, orchestration and
> governance** testable *before* investing in sophisticated autonomous design or engineering.
> The Product Owner and the specialist/governance agents are built in detail; the **Designer and
> Engineer are intentionally lightweight** placeholders with clear interfaces for later
> expansion.

---

## The reasoning kernel (five entities)

```
INTENT → OPPORTUNITY → PROPOSITION → TEST → LEARNING ↺
```

The loop is **recursive, not a pipeline**: Learning may update any earlier part of the model.
**Risk is not a sixth entity** — it is a continuous *assessment* across the whole model, owned
by the Product Owner, and it determines where attention goes.

- **Intent** — what we are trying to achieve. Typed hierarchy: **Challenge → Impact → Outcome**.
  The Challenge is human-governed. Outputs/features are not Outcomes.
- **Opportunity** — where there might be leverage (need, pain, desire, problem, unmet need).
  Opportunities are **not** Solutions.
- **Proposition** — what we believe, suspect, or must establish. One superclass with three
  types: **Claim | Assumption | Hypothesis**.
- **Test** — deliberate work to reduce a specified uncertainty in order to inform a decision.
  Every Test has a **Learning Objective** and an **Intended Decision Consequence**.
- **Learning** — an evidence-supported statement of what we learned and what it changes.
  Learning **must never exceed what its Evidence supports**.

**Evidence** is a supporting concept, not part of the kernel:
`Source / Raw Material → Evidence → Learning → Product Knowledge update`.
A prototype is not Evidence; observed interaction with a prototype may *produce* Evidence.
LLM confidence is not Evidence.

## The operating loop (distinct from the reasoning model)

```
Assess Risk → Set Sprint Goal → Select Tests/work → Execute → Capture Evidence
→ Produce Learning → Update Product Knowledge → Learning Accounting → Sprint Outcome
→ Pivot/Persevere → Next Sprint
```

There is **one shared Product Trio Sprint**.

## Agents (single OpenClaw instance)

All agents operate against shared **Product Knowledge**. See [AGENTS.md](AGENTS.md).

| Agent | Role |
|---|---|
| Product Owner | Intent, opportunity space, risk, prioritisation, Sprint Goal, Learning Accounting, Pivot/Reframe authority |
| Designer *(v1 light)* | Design perspective; usability/desirability uncertainty |
| Engineer *(v1 light)* | Technical reality; feasibility/constraints |
| Proposition Steward | The evolving belief model |
| Research Orchestrator | The operational lifecycle of Tests |
| Learning Steward | Integrity of canonical Learning |
| Product Scout | Sensing outside the current product model |
| AI Chief of Staff | Human attention & governance boundary (Management by Exception) |

## Repository map

| Path | Contents |
|---|---|
| `docs/methodology/` | The reasoning kernel, entities, evidence, risk, operating loop, principles |
| `docs/architecture/` | Topology, agents-as-responsibility, skills-vs-methodology |
| `docs/governance/` | Decision rights, escalation rules, Challenge governance, Decision Brief spec |
| `docs/operating-model/` | Operating loop, sprint model, Learning Accounting |
| `docs/adr/` | Architectural Decision Records |
| `agents/` | One responsibility charter per agent (`CHARTER.md`) |
| `skills/` | OpenClaw `SKILL.md` packages (reusable capabilities) |
| `schemas/` | JSON Schema (Draft 2020-12) for every Product Knowledge entity |
| `templates/` | Blank canonical records + Decision Brief |
| `canvases/` | Human-readable canvas projections |
| `governance/` | `decision_rights.yaml` — the single source of truth for who may do what |
| `examples/complaints/` | End-to-end worked example |
| `tests/` | Schema + governance checks (pytest) |
| `scripts/` | Validation & scaffolding helpers |
| `deploy/` | Single-instance OpenClaw config example |

## Core architectural principles

- **Agent boundaries represent persistent responsibility.** Knowledge survives the agent.
- **Skill boundaries represent reusable capability.** Methodologies live *inside* skills.
- **Deployment topology is separate from methodology.** OpenClaw boundaries are an
  implementation concern.
- Outputs are not Outcomes. Opportunities are not Solutions. A prototype is not Evidence.
- Every Test has a Learning Objective and an Intended Decision Consequence.
- Evidence requires provenance; Learning must not exceed Evidence.
- Risk determines attention. Progress means **Outcome movement and validated reduction of
  consequential uncertainty**.
- Humans retain authority over strategic **Challenge** changes.
- The AI Chief of Staff manages human attention and governance — **not** product truth.

The full canonical list is in [`docs/methodology/principles.md`](docs/methodology/principles.md).

## Running the checks

Requires Python 3.10+.

```bash
pip install -r scripts/requirements.txt      # jsonschema, pytest, pyyaml
pytest -q                                     # schema + governance + example checks
python scripts/validate.py examples/complaints  # validate the worked example records
```

Scaffold a new canonical record:

```bash
python scripts/new_record.py opportunity --title "Users cannot find their case reference"
```

## Status

This is **v1**. It deliberately optimises for validating the reasoning and learning system.
Designer and Engineer are lightweight by design (see their `CHARTER.md` and `INTERFACES.md`).
Later versions may substantially expand them without changing the reasoning kernel.

## Licence

[MIT](LICENSE).
