---
name: data-analytics
description: (v1 lightweight) Analyse existing quantitative data to produce observations as raw material for Evidence. Structure is complete; depth is deliberately limited in v1.
---

# Data Analytics  *(v1: deliberately lightweight)*

> ⚠️ **Deliberate v1 limitation.** This skill exists with a complete contract but a **shallow
> process** in v1. Huginn v1 focuses on validating product reasoning, learning and governance —
> not on deep analytics capability. The interface is stable so it can be **expanded later**
> (statistical rigour, experimentation platforms, causal inference) without changing how Evidence
> is produced. See [ADR 0011](../../docs/adr/0011-lightweight-designer-engineer.md) for the
> analogous Designer/Engineer decision.

## Purpose
Answer a Learning Objective from **existing quantitative data** (analytics, operational metrics,
support volumes) — producing observations that can become Evidence.

## When to use
- When a question can be answered from data already collected.

## When NOT to use
- When primary research is needed (`user-research`) or the analysis needs rigour beyond v1's
  shallow scope — flag it and keep the claim modest.

## Inputs
- A Learning Objective; access to the relevant dataset (as an artifact reference).

## Definition of Ready
- A specific question and an accessible, described dataset.

## Methodology selection (v1)
- Descriptive analysis and simple comparisons only. **No causal claims** from observational data
  in v1; note where stronger methods would be required.

## Process (v1)
1. Reference the dataset as an artifact (with provenance).
2. Produce descriptive observations relevant to the Learning Objective.
3. State limitations plainly (sampling, confounding, observational-only).
4. Hand observations + provenance to `evidence-appraisal`.

## Structured output
Artifact reference + descriptive observations with limitations.

## Quality criteria
- Claims stay descriptive; limitations are explicit; provenance complete.

## Definition of Done
- Appraisable descriptive observations, with over-reach avoided.

## Failure modes
- Inferring causation from correlation.
- Over-claiming beyond v1's descriptive scope.

## Escalation / governance
- If a decision needs rigour beyond v1 analytics, escalate rather than over-claim.
