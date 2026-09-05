# ADR 0004 — "Learning" replaces "Finding"

**Status:** Accepted

## Context
"Finding" connotes a discovered fact and invites over-claiming — a single observation becoming a
truth. Huginn's discipline is that conclusions stay within their evidence and are explicitly about
*what changes*.

## Decision
The kernel entity is **Learning**, not "Finding". A Learning is an **evidence-supported statement
of what we learned and what it changes**, carrying supporting Evidence, provenance, limitations,
confidence, implications and affected entities. **Learning must never exceed its Evidence.**

## Consequences
- `schemas/learning.schema.json` requires `evidence` (≥1), `limitations` and `provenance`.
- `tests/test_learning_evidence.py` enforces that Learning cannot stand on nothing.
- The Learning Steward controls admission into canonical Product Knowledge.
- Language shift reinforces humility: we *learned* X (bounded), not *found* X (absolute).
