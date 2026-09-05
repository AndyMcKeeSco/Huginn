---
name: pivot-persevere-assessment
description: Decide at sprint end whether to persevere, adjust within the frame, or (Product Owner only) recommend a Pivot/Reframe to a human.
---

# Pivot / Persevere Assessment

## Purpose
Make the explicit end-of-sprint call: **persevere**, **adjust** within the current frame, or
**recommend a Pivot/Reframe** to a human — based on Learning Accounting and the risk picture.

## When to use
- At the close of every sprint.

## When NOT to use
- Mid-sprint as a reaction to a single data point.
- To enact a Challenge change (human-reserved).

## Inputs
- Sprint Outcome; Learning Accounting; updated beliefs and risk; Scout signals.

## Definition of Ready
- A closed sprint with a Learning Accounting record.

## Methodology selection
- **Build–Measure–Learn / Pivot-or-Persevere**; **Innovation Accounting**; riskiest-assumption
  status.

## Process
1. Review learning-per-cost and Outcome movement.
2. If the frame holds and progress is real → **persevere**.
3. If the frame holds but the approach should change → **adjust**.
4. If Learning suggests the frame (up to the Challenge) may be wrong → the Product Owner
   originates a **Pivot/Reframe Recommendation** to a human.
5. Record a Pivot/Persevere Review.

## Structured output
A Pivot/Persevere Review (`schemas/pivot-persevere-review.schema.json`); when recommending, a
Pivot/Reframe Recommendation (`schemas/pivot-reframe-recommendation.schema.json`).

## Quality criteria
- The decision follows from the account and risk, not sentiment; recommendations cite Learning.

## Definition of Done
- A recorded, justified persevere/adjust/recommend decision.

## Failure modes
- Persevering out of sunk cost; pivoting on noise.
- An agent other than the Product Owner originating a Pivot/Reframe (forbidden).

## Escalation / governance
- Only the Product Owner may `originate_pivot_reframe`; only a human may `decide_pivot_reframe`;
  the AI Chief of Staff routes it (`docs/governance/challenge-governance.md`).
