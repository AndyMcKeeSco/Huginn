---
name: learning-synthesis
description: Synthesise appraised Evidence into Learning statements with implications and affected entities, triangulating across sources.
---

# Learning Synthesis

## Purpose
Combine appraised **Evidence** into **Learning** — evidence-supported statements of what Huginn
has learned and what it changes — triangulating across independent sources.

## When to use
- Once enough Evidence exists to say something about a Learning Objective.

## When NOT to use
- To validate the claim's bounds (use `learning-validation`).
- To admit into canonical Product Knowledge (that is admission control).

## Inputs
- Appraised Evidence records; the Learning Objective; affected Propositions/Opportunities.

## Definition of Ready
- One or more Evidence records bearing on the objective.

## Methodology selection
- **Evidence synthesis & Triangulation**; **adapted GRADE** to grade the body of Evidence.

## Process
1. Group Evidence bearing on the same question.
2. Draft a Learning `statement` that the Evidence supports.
3. Triangulate across independent sources; note where they agree/conflict.
4. State `implications` and `affected_entities`; set draft `strength`/`confidence`.

## Structured output
Draft Learning records (`schemas/learning.schema.json`, `canonical: false`) for validation.

## Quality criteria
- Every clause traces to Evidence; triangulation is explicit; implications are concrete.

## Definition of Done
- A draft Learning ready for `learning-validation`.

## Failure modes
- Synthesising beyond the Evidence.
- Ignoring conflicting Evidence in the synthesis.

## Escalation / governance
- Synthesis produces drafts only; admission is controlled by `learning-validation` + the Learning
  Steward.
