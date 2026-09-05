# ADR 0002 — Intent hierarchy: Challenge → Impact → Outcome

**Status:** Accepted

## Context
"What are we trying to achieve?" spans strategic ambition down to measurable change. Conflating
these levels lets outputs masquerade as goals and blurs where human authority sits.

## Decision
Intent is a **typed hierarchy**: **Challenge → Impact → Outcome**.
- **Challenge** — the strategic problem/ambition; **human-governed** (ADR 0016).
- **Impact** — the higher-order effect expected on success.
- **Outcome** — a **measurable behavioural or real-world change** (requires a `measure`).
Outputs/features are explicitly **not** Outcomes.

## Consequences
- `schemas/intent.schema.json` enforces the typing: a Challenge is `human_governed` and parentless;
  an Outcome requires a `measure`; Impact/Outcome require a parent.
- `tests/test_intent_hierarchy.py` enforces these rules.
- Provides a clean anchor for traceability and for reserving strategic authority to humans.
