# ADR 0001 — Five-entity reasoning kernel

**Status:** Accepted

## Context
Product-development systems accrete concepts. A large ontology is expressive but hard to reason
over, hard to govern, and easy to drift. Huginn must be *machine-operable* and *testable*.

## Decision
Huginn's reasoning kernel has exactly **five entities**: **Intent, Opportunity, Proposition,
Test, Learning**, connected as `Intent → Opportunity → Proposition → Test → Learning ↺`. All
other concepts (Evidence, Risk, Solution, Decision, Sprint, Canvas, …) are **supporting
machinery** arranged around the kernel, not kernel entities.

## Consequences
- Keeps the model small enough to reason over and to validate with schemas + tests.
- Forces new concepts to justify themselves as supporting machinery rather than kernel members.
- The kernel is recursive, not a pipeline (see [ADR 0007](0007-reasoning-loop-vs-operating-loop.md)).
- Evidence and Risk are deliberately excluded from the kernel (ADRs 0006 and `evidence.md`).
