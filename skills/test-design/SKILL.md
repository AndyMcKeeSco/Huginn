---
name: test-design
description: Design a Test that reduces a specified uncertainty at least cost, with a Learning Objective, evidence sought, method and an Intended Decision Consequence.
---

# Test Design

## Purpose
Design a **Test** that is the **least costly sufficiently reliable** way to reduce a specified
uncertainty — and that will actually change a decision.

## When to use
- When a riskiest assumption / consequential uncertainty needs reducing.

## When NOT to use
- When no decision hinges on the result (then it is not worth running).
- To check readiness (use `test-readiness`).

## Inputs
- The target Proposition/uncertainty; its consequence; available methods and budget.

## Definition of Ready
- A named uncertainty with a decision attached to its resolution.

## Methodology selection
- **Riskiest Assumption Testing**; **Build–Measure–Learn**; **Design of Experiments** where
  quantitative rigour is warranted; cheaper methods (interview, fake door, concierge, desk
  research) when they are *sufficiently* reliable.

## Process
1. State the **Learning Objective** (the uncertainty to reduce).
2. Name the **target** Proposition(s)/uncertainty.
3. Define **evidence sought** (what observation would count).
4. Choose the cheapest **method** that is reliable enough for the decision.
5. State the **Intended Decision Consequence** ("if we learn X we will do Y").
6. Record a `reliability_rationale` and `cost_estimate`.

## Structured output
A Test record (`schemas/test.schema.json`) with all required fields.

## Quality criteria
- Learning Objective and Intended Decision Consequence present and meaningful.
- Method is the cheapest sufficiently reliable option.

## Definition of Done
- A Test that, whatever the result, changes what the Trio does next.

## Failure modes
- Research theatre (no decision attached).
- Over-engineered reliability; confirmation-seeking design.

## Escalation / governance
- Tests missing a Learning Objective or Intended Decision Consequence are rejected by the schema
  and tests.
