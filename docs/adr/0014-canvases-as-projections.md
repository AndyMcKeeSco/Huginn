# ADR 0014 — Canvases as projections, not truth

**Status:** Accepted

## Context
Canvases (Lean Product, Value Proposition, Opportunity Solution Tree, etc.) are valuable for human
communication, but if treated as canonical they duplicate truth and can drift from the underlying
records, and if treated as gates they distort the operating loop.

## Decision
Canvases are **human-readable projections of Product Knowledge**. They are **not** canonical truth
and **not** lifecycle gates. **Every canvas element references canonical records by id.**

## Consequences
- `schemas/canvas.schema.json` requires each element to carry `refs` (≥1 canonical id).
- `tests/test_canvas_refs.py` enforces referential integrity (no orphan facts).
- Canvases can always be regenerated from — and traced back to — Product Knowledge.
- Ten canvas types are supported; see `canvases/README.md`.
