---
name: assumption-mapping
description: Map the assumptions underpinning an Opportunity, Solution or decision by importance and evidence, to expose the riskiest assumptions to test first.
---

# Assumption Mapping

## Purpose
Surface the **Assumptions** a plan rests on and rank them by **importance × uncertainty** so the
**riskiest assumptions** get tested first.

## When to use
- When committing to a Target Opportunity, Solution direction or decision.
- Before a Sprint, to choose what to learn.

## When NOT to use
- To design the Test itself (use `test-design`).

## Inputs
- The Opportunity/Solution/decision; existing Propositions; current belief state.

## Definition of Ready
- A specific plan/decision whose assumptions can be enumerated.

## Methodology selection
- **Assumption Mapping** (importance vs evidence 2×2).
- **Riskiest Assumption Testing** to prioritise the top-right quadrant.

## Process
1. Enumerate assumptions (as Assumption-type Propositions).
2. Rate each on importance (consequence if false) and current evidence/confidence.
3. Plot; identify high-importance / low-evidence assumptions as riskiest.
4. Hand the riskiest to `test-design` / the Product Owner's risk view.

## Structured output
An assumption map with a ranked riskiest-assumptions list, linked to Proposition records.

## Quality criteria
- Assumptions are load-bearing and atomic; ranking reflects consequence and evidence.

## Definition of Done
- The riskiest assumptions are explicit and prioritised for learning.

## Failure modes
- Listing comfortable assumptions, not load-bearing ones.
- Rating by gut with no reference to evidence/confidence.

## Escalation / governance
- Feeds `risk-assessment`; prioritisation of what to test remains the Product Owner's.
