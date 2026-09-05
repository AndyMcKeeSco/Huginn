---
name: proposition-formation
description: Form well-stated Propositions (Claim, Assumption, Hypothesis) with a clear statement, initial epistemic state and provenance.
---

# Proposition Formation

## Purpose
Create crisp **Propositions** — the units of belief Huginn reasons over. A good Proposition is a
single, testable-or-checkable statement with a clear type and honest starting confidence.

## When to use
- When an Opportunity, Solution or decision rests on something that must be true.
- When a signal or observation raises something worth believing/checking.

## When NOT to use
- To classify an existing Proposition's type (use `proposition-classification`).
- To test a Proposition (use `test-design`).

## Inputs
- The source idea/need/assumption; context; any prior related Propositions.

## Definition of Ready
- A specific statement to capture; a candidate type in mind.

## Methodology selection
- **Assumption mapping / Lean UX hypotheses** to phrase testable statements.
- One assertion per Proposition; avoid compound statements.

## Process
1. Write a single-sentence `statement`.
2. Set `type` (claim/assumption/hypothesis) — refine via `proposition-classification` if unsure.
3. Set `epistemic_state: open` and an honest initial `confidence`.
4. Record provenance; link to the Opportunity/Solution/decision it serves.

## Structured output
Proposition records (`schemas/proposition.schema.json`).

## Quality criteria
- Atomic, unambiguous statement; type and confidence justified.

## Definition of Done
- A valid Proposition the Steward can track and the Orchestrator can target.

## Failure modes
- Compound or vague statements.
- Overconfident starting confidence with no basis.

## Escalation / governance
- Candidates may come from Scout/PO; the Proposition Steward owns the canonical record.
