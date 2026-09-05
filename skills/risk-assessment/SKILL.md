---
name: risk-assessment
description: Assess the most consequential uncertainty between Huginn and its target Outcome, selecting an appropriate lens rather than one hard-coded formula.
---

# Risk Assessment

## Purpose
Answer the Product Owner's standing question — *"What is the most consequential uncertainty
currently standing between us and the intended Outcome?"* — and rank uncertainty to **direct
attention**.

## When to use
- Continuously; especially at the start of the operating loop each sprint.

## When NOT to use
- As a lifecycle gate or a single vanity score.

## Inputs
- Intent/Outcomes; belief state (confidence, epistemic state); assumption maps; Learnings;
  Scout signals.

## Definition of Ready
- A target Outcome and a current belief model.

## Methodology selection (choose, don't hard-code)
- **Riskiest-assumption thinking**; **Expected Value of Information**; **decision analysis**;
  **RICE/WSJF** where useful. Dimensions may include uncertainty, consequence, value,
  desirability, usability, feasibility, viability, delivery, operational risk, cost of being
  wrong, cost of learning, time to learning.

## Process
1. Enumerate live uncertainties (from assumptions, contradictions, signals).
2. Weigh consequence × uncertainty (and cost/time to learn) with a chosen lens.
3. Rank; name the single most consequential uncertainty.
4. Record a Decision (`decision_type: risk_assessment`) with the lens and rationale.

## Structured output
A ranked risk view + a Decision record; the top item frames the Sprint Goal.

## Quality criteria
- The lens and rationale are explicit; the ranking ties to the Outcome; no hidden formula.

## Definition of Done
- The most consequential uncertainty is named and justified.

## Failure modes
- One universal score masking judgement.
- Ranking by effort or preference instead of consequence.

## Escalation / governance
- High-consequence uncertainty that cannot be reduced autonomously escalates via the AI Chief of
  Staff.
