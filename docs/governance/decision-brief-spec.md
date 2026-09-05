# Decision Brief — Specification

A **Decision Brief** is the AI Chief of Staff's structured output at the boundary between
autonomous operation and human attention. It is **concise but fully traceable** back to canonical
Product Knowledge. The machine-operable schema is
[`schemas/decision-brief.schema.json`](../../schemas/decision-brief.schema.json); the template is
[`templates/decision-brief.template.yaml`](../../templates/decision-brief.template.yaml).

A brief is produced for **both** outcomes of an exception assessment:

- `escalate: true` — a human must be involved.
- `escalate: false` — a considered decision that routine handling is sufficient (recorded, not
  silent).

## Required content

| Field | Meaning | Required when |
|---|---|---|
| `authored_by` | Fixed: `ai-chief-of-staff`. | always |
| `escalate` | Whether a human is required. | always |
| `trigger` | Which exception condition fired. | always |
| `what_happened` | The event, plainly. | always |
| `why_it_matters` | Consequence and relevance to Intent/Outcome. | always |
| `relevant_intent` | The Intent/Outcome(s) in play. | recommended |
| `relevant_evidence_learning` | Canonical Evidence/Learning ids. | recommended |
| `current_uncertainty` | What remains unresolved. | recommended |
| `agent_recommendations` | Each agent's recommendation. | when escalating |
| `material_disagreements` | Where agents disagree. | when present |
| `options` | Options with likely consequences. | when escalating |
| `decision_required` | The decision the human must make. | when escalating |
| `urgency` | low / medium / high / critical. | when escalating |
| `decision_authority` | Who holds the decision (often `human`). | when escalating |
| `no_escalation_rationale` | Why routine handling suffices. | when **not** escalating |
| `provenance` | Authoring provenance. | always |

The schema enforces the conditional requirements: an escalating brief must carry
`decision_required`, `urgency`, `decision_authority` and `options`; a non-escalating brief must
carry `no_escalation_rationale`.

## Design intent

- **Traceable, not verbose.** Every claim points at a canonical id; the human can drill in.
- **Decision-first.** An escalating brief states the decision and the options, not a narrative.
- **Honest about disagreement.** Material disagreements are surfaced, not smoothed over.
- **Authority-explicit.** The brief names who decides, so the boundary is never ambiguous.

## What a brief must never do

- Change Intent or the Challenge.
- Originate a Pivot/Reframe Recommendation (that is the Product Owner's; the brief may *carry*
  one to a human).
- Substitute the ACoS's judgement for the Product Owner's product decisions.
