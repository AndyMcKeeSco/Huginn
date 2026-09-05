---
name: belief-revision
description: Revise a Proposition's confidence and epistemic state in the light of admitted Learning, using Bayesian/weight-of-evidence updating and recording the revision.
---

# Belief Revision

## Purpose
Update belief — `confidence` and `epistemic_state` — on a Proposition when **admitted canonical
Learning** bears on it, and propagate consequences to dependent Propositions.

## When to use
- Whenever the Learning Steward admits a Learning affecting a Proposition.

## When NOT to use
- On raw material, un-admitted findings, or LLM assertions (LLM confidence is not Evidence).

## Inputs
- The Proposition; the admitted Learning (with strength) supporting/contradicting it.

## Definition of Ready
- Learning is canonical (`canonical: true`) and links to the Proposition.

## Methodology selection
- **Bayesian updating / Bayes factors / Weight of Evidence** to move confidence in proportion to
  evidential strength and independence.
- **Truth Maintenance** to propagate to `depends_on` Propositions.

## Process
1. Add the Learning to `supporting_learning` or `contradicting_learning`.
2. Update `confidence` proportionate to strength; never discard contradicting Learning.
3. Update `epistemic_state` (open → supported/contradicted/mixed; retire when settled).
4. Append a `history` entry (from → to, by, evidence).
5. Propagate to dependent Propositions and flag material changes for the Product Owner.

## Structured output
Updated Proposition (confidence, epistemic_state, history) and any propagated updates.

## Quality criteria
- Movement is justified by evidential weight; history is complete; contradictions retained.

## Definition of Done
- Belief reflects the current admitted Evidence; dependents are consistent.

## Failure modes
- Confidence drift without Evidence; dropping contradicting Learning; overwriting history.

## Escalation / governance
- `revise_belief` is the Proposition Steward's right; irreconcilable contradiction escalates to
  the AI Chief of Staff.
