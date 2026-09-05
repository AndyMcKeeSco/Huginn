# ADR 0006 — Risk as continuous assessment, not a kernel entity

**Status:** Accepted

## Context
Risk is central to prioritisation, but modelling it as a first-class kernel entity would bloat the
kernel and imply risk is a *thing to manage* rather than a *lens for directing attention*.

## Decision
**Risk is a continuous assessment across the whole product model, owned by the Product Owner** —
not a sixth kernel entity. Its purpose is to **direct attention** to the most consequential
uncertainty. Huginn does **not** hard-code one universal scoring formula; the Risk Assessment
skill selects an appropriate lens and shows its working.

## Consequences
- The kernel stays at five entities (ADR 0001).
- Risk assessments are recorded as **Decisions** (`decision_type: risk_assessment`) and referenced
  from Sprints, so "why this focus, why now" is auditable.
- The operating loop begins with "Assess Risk" (ADR 0007).
- See `docs/methodology/risk.md`.
