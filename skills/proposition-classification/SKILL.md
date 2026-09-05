---
name: proposition-classification
description: Classify a Proposition as Claim, Assumption or Hypothesis, and reclassify as its role changes.
---

# Proposition Classification

## Purpose
Assign the correct **type** to a Proposition — Claim (assertion about the world), Assumption
(must be true to succeed), or Hypothesis (testable prediction) — because type shapes how it is
treated and tested.

## When to use
- Right after formation, or when a Proposition's role changes.

## When NOT to use
- To form the statement (use `proposition-formation`).

## Inputs
- The Proposition statement and its context/role.

## Definition of Ready
- A statement exists.

## Methodology selection
- Decision rule:
  - Does something *depend* on it being true to succeed? → **Assumption**.
  - Is it a *prediction* we could test? → **Hypothesis**.
  - Is it an *assertion about the world* we hold? → **Claim**.

## Process
1. Apply the decision rule; pick the single best-fit type.
2. If it is load-bearing for a decision, note the dependency (feeds `assumption-mapping`).
3. Update `type`; record the reclassification in history if changed.

## Structured output
Updated Proposition `type` (+ history entry on change).

## Quality criteria
- Type matches the decision rule; only the three valid types are used.

## Definition of Done
- Every active Proposition carries a justified type.

## Failure modes
- Labelling everything a "hypothesis".
- Silent reclassification with no history.

## Escalation / governance
- Unsupported types are rejected by `schemas/proposition.schema.json` and the tests.
