---
name: opportunity-discovery
description: Discover user/customer needs, pains, desires and problems as candidate Opportunities (never solutions), grounded in evidence of existence.
---

# Opportunity Discovery

## Purpose
Surface **Opportunities** — needs, pains, desires, problems, unmet needs and areas of leverage —
that could move an Outcome. Opportunities are *not* solutions.

## When to use
- When the Opportunity Space is thin, stale, or solution-biased.
- After new research, signals, or Outcome movement.

## When NOT to use
- To evaluate or choose among Opportunities (use `opportunity-assessment` / `-selection`).
- To propose solutions.

## Inputs
- Target Outcome(s); research corpus; Product Scout signals; support data.

## Definition of Ready
- At least one measurable Outcome to discover leverage toward.

## Methodology selection
- **Continuous Discovery** and **Jobs To Be Done** to frame needs as jobs/struggles.
- **Weak-signal detection** when drawing on Product Scout material.

## Process
1. Gather candidate needs/pains from research, tickets, interviews, signals.
2. Phrase each as an Opportunity (a need/problem), not a solution.
3. Attach `evidence_of_existence` where available; mark unevidenced ones as candidates.
4. Set `opportunity_type` and `role: candidate`; link `intent_ref`.

## Structured output
Opportunity records (`schemas/opportunity.schema.json`) with `role: candidate`, ready for mapping
and assessment.

## Quality criteria
- No solution language ("add X"); each item is a genuine need/problem.
- Existence is evidenced or explicitly flagged as unevidenced.

## Definition of Done
- A set of candidate Opportunities linked to an Outcome, ready to map.

## Failure modes
- Solutions disguised as Opportunities.
- Asserting needs with no evidence and not flagging them.

## Escalation / governance
- The Product Scout may introduce candidates but must not change direction; adoption is the
  Product Owner's (`governance/decision_rights.yaml`).
