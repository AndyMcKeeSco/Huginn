# Agents

Huginn runs as **one OpenClaw instance** containing the agents below. All agents operate
against shared **Product Knowledge** (see `schemas/`, `templates/`). Deployment topology is an
implementation concern documented in [`docs/adr/0009-single-openclaw-instance-topology.md`](docs/adr/0009-single-openclaw-instance-topology.md)
and mapped in [`deploy/openclaw.config.example.json5`](deploy/openclaw.config.example.json5).

**Agent boundaries represent persistent responsibility.** Each agent has a durable charter in
`agents/<name>/CHARTER.md`. Reusable capability lives in `skills/` — methodologies live inside
skills, not in agents. See [`docs/architecture/agents-as-responsibility.md`](docs/architecture/agents-as-responsibility.md).

Decision rights are enforced from a single source of truth:
[`governance/decision_rights.yaml`](governance/decision_rights.yaml).

## Core Product Trio

| Agent | Owns | Core question | Charter |
|---|---|---|---|
| **Product Owner** | Intent, Opportunity Space, Target Opportunity, risk assessment, prioritisation, Sprint Goal, Learning Accounting, Pivot/Persevere Review, **sole Pivot/Reframe Recommendation authority** | *What is currently most likely to stop us achieving the intended Outcome, and what should we learn or do next to reduce that risk?* | [charter](agents/product-owner/CHARTER.md) |
| **Designer** *(v1 lightweight)* | Design perspective; usability/desirability uncertainty | *Where might design uncertainty stop us, and what light design activity would reduce it?* | [charter](agents/designer/CHARTER.md) · [interfaces](agents/designer/INTERFACES.md) |
| **Engineer** *(v1 lightweight)* | Technical/engineering reality; feasibility uncertainty | *Where might technical reality stop us, and what light investigation would reduce that uncertainty?* | [charter](agents/engineer/CHARTER.md) · [interfaces](agents/engineer/INTERFACES.md) |

## Specialist agents

| Agent | Owns | Core question | Charter |
|---|---|---|---|
| **Proposition Steward** | The evolving belief model: Claims, Assumptions, Hypotheses, confidence, epistemic state, relationships, contradictions, history, belief revision | *Given the Evidence, what should we now believe, and how strongly?* | [charter](agents/proposition-steward/CHARTER.md) |
| **Research Orchestrator** | The operational lifecycle of Tests: design coordination, readiness, sequencing, dependencies, WIP, routing, retries, remediation | *What is the least costly sufficiently reliable Test to run next, and is it ready?* | [charter](agents/research-orchestrator/CHARTER.md) |
| **Learning Steward** | Integrity of canonical Learning: Evidence appraisal, synthesis, validation, provenance, triangulation, admission control | *Does this conclusion follow from the Evidence, and may it enter canonical Product Knowledge?* | [charter](agents/learning-steward/CHARTER.md) |
| **Product Scout** | Sensing outside the current product model: emerging needs, market/competitor/regulatory/technology change, weak signals | *What has changed outside our model that our current beliefs may not account for?* | [charter](agents/product-scout/CHARTER.md) |

## Governance / attention

| Agent | Owns | Core question | Charter |
|---|---|---|---|
| **AI Chief of Staff** | The boundary between autonomous operation and scarce human attention; escalation, Decision Briefs, cross-agent coherence, governance enforcement | *What does the human need to know, decide, approve or intervene in now?* | [charter](agents/ai-chief-of-staff/CHARTER.md) |

## Decision-rights summary

| Action | Authority |
|---|---|
| Change the **Challenge** | **Human only** (no agent may) |
| Change Impact / Outcome | Product Owner (proposes; governed changes may require human) |
| Select Target Opportunity | Product Owner |
| Propose Sprint Goal | Product Owner |
| Originate a **Pivot/Reframe Recommendation** | **Product Owner only** |
| Introduce signals / candidate Opportunities & Propositions | Product Scout (may **not** change direction or issue a Challenge pivot) |
| Admit Learning into canonical Product Knowledge | Learning Steward |
| Revise belief / confidence on a Proposition | Proposition Steward |
| Escalate to a human via a Decision Brief | AI Chief of Staff (may **not** change Intent/Challenge, own PO decisions, or originate a Pivot/Reframe) |

The machine-readable form of this table is [`governance/decision_rights.yaml`](governance/decision_rights.yaml),
which the tests in `tests/` enforce.
