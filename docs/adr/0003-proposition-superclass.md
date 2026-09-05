# ADR 0003 — Proposition superclass (Claim | Assumption | Hypothesis)

**Status:** Accepted

## Context
Claims, assumptions and hypotheses share almost all machinery — an id, a statement, confidence,
epistemic state, supporting/contradicting evidence, relationships, provenance and history — but
differ in role. Modelling them as three unrelated types would duplicate machinery and fragment
belief revision.

## Decision
Model them as **one superclass, `Proposition`, with a `type` of `claim`, `assumption` or
`hypothesis`.** All three share identical machinery; `type` captures the difference in role.

## Consequences
- One code path for belief revision, contradiction detection and confidence.
- `schemas/proposition.schema.json` restricts `type` to the three values; unsupported types fail
  (`tests/test_proposition_types.py`).
- The Proposition Steward owns the single evolving belief model.
