---
name: learning-validation
description: Validate that a draft Learning does not exceed its Evidence, has honest limitations and complete provenance, then control admission into canonical Product Knowledge.
---

# Learning Validation

## Purpose
Guard the cardinal rule — **Learning must never exceed its Evidence** — and control **admission**
of Learning into canonical Product Knowledge.

## When to use
- On every draft Learning before it becomes canonical.

## When NOT to use
- To create the Learning (use `learning-synthesis`).

## Inputs
- A draft Learning and its Evidence.

## Definition of Ready
- A draft Learning with linked Evidence and stated limitations.

## Methodology selection
- **Critical appraisal / adapted GRADE**; **Triangulation**; provenance/lineage checks.

## Process
1. Check each claim is supported by the linked Evidence — trim anything that over-reaches.
2. Verify `limitations` honestly bound the claim.
3. Verify provenance/lineage back to raw material.
4. Set final `strength`/`confidence`; if it passes, set `canonical: true`
   (`admit_canonical_learning`). Otherwise return to synthesis or commission more Evidence.

## Structured output
A validated, canonical Learning (or a rejection with reasons).

## Quality criteria
- No claim exceeds its Evidence; limitations present; provenance complete.

## Definition of Done
- Only Evidence-bounded Learning enters canonical Product Knowledge.

## Failure modes
- Admitting over-claiming Learning under pressure.
- Waving through weak provenance.

## Escalation / governance
- `admit_canonical_learning` is the Learning Steward's sole right; pressure to over-admit is a
  governance concern for the AI Chief of Staff.
