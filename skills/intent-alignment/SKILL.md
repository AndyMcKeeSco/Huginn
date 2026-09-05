---
name: intent-alignment
description: Check that Opportunities, Propositions, Tests and work trace to a measurable Outcome, and surface anything that has drifted away from Intent.
---

# Intent Alignment

## Purpose
Keep the whole product model **traceable to Intent**. Verify that Opportunities offer leverage on
an Outcome, that Tests reduce uncertainty that matters to an Outcome, and flag orphaned or
drifted work.

## When to use
- During Sprint planning and review.
- When new Opportunities/Propositions/Tests are added.
- Periodically, to detect drift.

## When NOT to use
- To *create* Intent (use `intent-definition`).
- To decide priority (use `risk-assessment` / `opportunity-selection`).

## Inputs
- Current Intent hierarchy, Opportunity Space, Propositions, Tests, Sprint.

## Definition of Ready
- Intent records exist with measurable Outcomes.

## Methodology selection
- **Impact Mapping** and **Opportunity Solution Trees** as the traceability backbone.
- Traceability chain: Intent → Opportunity → Proposition → Test → Evidence → Learning.

## Process
1. For each active Opportunity, confirm an `intent_ref` to an Outcome/Impact.
2. For each active Test, confirm its target Proposition/uncertainty ties back to an Outcome.
3. List orphans (no path to an Outcome) and drift (work whose Outcome link is stale).
4. Recommend re-link, re-scope, or retire — for the Product Owner to decide.

## Structured output
An alignment report: linked / orphaned / drifted items, with recommendations. Feeds the Product
Owner; may annotate the Intent/Outcomes canvas.

## Quality criteria
- Every active item is classified; recommendations are actionable and reference ids.

## Definition of Done
- Orphans and drift surfaced; the Product Owner has a clear re-alignment list.

## Failure modes
- Declaring alignment by assertion rather than by tracing links.
- Silently retiring work instead of recommending it.

## Escalation / governance
- Alignment does not change priority or Intent; it informs the Product Owner, who decides.
