# ADR 0015 — Learning Accounting

**Status:** Accepted

## Context
Traditional delivery metrics (velocity, output volume) reward activity, not progress. Huginn
defines progress as **Outcome movement and validated reduction of consequential uncertainty**, so
it needs an accounting method that measures *learning*, adapted from Eric Ries's Innovation
Accounting.

## Decision
Each sprint is closed with **Learning Accounting** (owned by the Product Owner): an account of how
much consequential uncertainty was reduced, whether the target Outcome moved, and whether that was
worth the cost. It references admitted Learnings, the affected Propositions' before/after belief,
and the Sprint. It is **not** a velocity/output count and **not** a single universal score.

## Consequences
- Recorded as a Decision (`decision_type: learning_accounting`), feeding the Sprint Outcome and
  Pivot/Persevere Review.
- A run of near-zero learning-per-cost is an escalation signal.
- See `docs/operating-model/learning-accounting.md` and `skills/learning-accounting/`.
