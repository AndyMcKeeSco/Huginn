---
name: learning-accounting
description: Account for a sprint's progress as consequential uncertainty reduced and Outcome movement relative to cost — Innovation Accounting adapted for Huginn.
---

# Learning Accounting

## Purpose
Account for **progress as learning**: how much consequential uncertainty a sprint reduced, whether
the target Outcome moved, and whether that was worth the cost. Adapts Eric Ries's Innovation
Accounting.

## When to use
- At each Sprint review, before Pivot/Persevere.

## When NOT to use
- As a velocity/output metric.

## Inputs
- The Sprint; admitted Learnings; affected Propositions' before/after belief; cost of the sprint.

## Definition of Ready
- A closed sprint with admitted Learnings.

## Methodology selection
- **Innovation Accounting**; **Expected Value of Information** (retrospective sanity check).

## Process
1. Identify which Propositions changed state/confidence and how much that mattered.
2. Assess Outcome movement (or why it will not move).
3. Weigh reduction against the sprint's cost.
4. Record the account, referencing Learnings, Propositions and the Sprint.

## Structured output
A Learning Accounting record (a Decision, `decision_type: learning_accounting`) feeding the
Sprint Outcome and Pivot/Persevere Review.

## Quality criteria
- Every claimed reduction traces to admitted Learning; cost is included; no output-counting.

## Definition of Done
- An honest account of learning-per-cost for the sprint.

## Failure modes
- Counting activity/output as progress.
- Claiming reduction with no Learning behind it.

## Escalation / governance
- Feeds Pivot/Persevere; a run of near-zero learning-per-cost is an escalation signal.
