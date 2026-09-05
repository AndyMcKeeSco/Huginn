---
name: contradiction-detection
description: Detect Propositions, Learnings or signals that are in tension, and surface them for reconciliation or escalation.
---

# Contradiction Detection

## Purpose
Find where beliefs and Evidence **conflict** — Propositions in tension, Learnings that disagree,
or signals that invalidate an Assumption — so they are reconciled rather than silently coexisting.

## When to use
- After belief revision or new Learning/signals.
- Periodically across the Proposition set.

## When NOT to use
- To resolve the contradiction (that is belief revision / risk / escalation).

## Inputs
- Propositions with relationships; canonical Learnings; Product Scout signals.

## Definition of Ready
- A belief model with relationships exists.

## Methodology selection
- **Truth Maintenance / consistency checking** across `contradicts` and `depends_on` edges.
- **Evidence triangulation** to spot disagreeing Learnings.

## Process
1. Scan for `contradicts` edges and for opposing statements not yet linked.
2. Check whether new Learning contradicts existing supported Propositions.
3. Check Scout signals against load-bearing Assumptions (`may_invalidate`).
4. Record contradictions and rate their consequence.

## Structured output
A contradiction report: pairs/sets in tension, consequence, and a recommended route
(reconcile / test / escalate).

## Quality criteria
- Real tensions (not mere differences) identified; consequence rated.

## Definition of Done
- Contradictions surfaced with a route; none left latent.

## Failure modes
- Missing indirect contradictions via dependencies.
- Crying contradiction on non-conflicting nuance.

## Escalation / governance
- Major, high-consequence contradictions escalate to the AI Chief of Staff for the Product
  Owner's attention.
