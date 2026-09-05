---
name: opportunity-selection
description: Select the Target Opportunity (role=target) for the Product Trio to focus on, based on assessment and current risk. Product Owner decision.
---

# Opportunity Selection

## Purpose
Choose the **Target Opportunity** — the focus of the Product Trio — and mark it `role: target`,
based on assessment and the current risk picture.

## When to use
- At Sprint planning, or when risk shifts enough to change focus.

## When NOT to use
- To assess or map (upstream skills).
- Without a current risk assessment.

## Inputs
- Opportunity assessments; current `risk-assessment`; target Outcome.

## Definition of Ready
- Opportunities are assessed and a risk view exists.

## Methodology selection
- **Riskiest-assumption thinking** — favour the Opportunity whose resolution most reduces
  consequential uncertainty toward the Outcome.
- **Expected Value of Information** where the cost/benefit of learning is estimable.

## Process
1. Combine leverage, evidence and consequential uncertainty.
2. Choose the Opportunity that best advances the Outcome given current risk.
3. Set the chosen Opportunity `role: target`; demote the previous target if any.
4. Record a Decision (`decision_type: target_opportunity`) with rationale.

## Structured output
The updated Opportunity (`role: target`) and a Decision record capturing the choice.

## Quality criteria
- Exactly one Target per focus; the rationale ties to risk and the Outcome.

## Definition of Done
- A Target Opportunity set and recorded, ready to frame a Sprint Goal.

## Failure modes
- Selecting on novelty or preference rather than risk-adjusted leverage.
- Leaving multiple ambiguous targets.

## Escalation / governance
- `select_target_opportunity` is the Product Owner's right (`governance/decision_rights.yaml`).
