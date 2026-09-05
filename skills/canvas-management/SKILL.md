---
name: canvas-management
description: Build and maintain human-readable canvases as projections of canonical Product Knowledge, where every element references real records.
---

# Canvas Management

## Purpose
Create and keep **canvases** — human-readable projections of Product Knowledge. Canvases are
**not** canonical truth and **not** lifecycle gates; every element references canonical records.

## When to use
- To communicate state to humans (Intent, Opportunity tree, risk, sprint history, value prop…).
- When canonical records change and a canvas needs refreshing.

## When NOT to use
- As a source of truth or an approval gate.
- To store data that lives nowhere else (canvases only *project*).

## Inputs
- Canonical records (Intent, Opportunities, Propositions, Learnings, Sprints…).

## Definition of Ready
- The records to be projected exist and have stable ids.

## Methodology selection
- Choose the canvas type for the audience/purpose (see `schemas/canvas.schema.json` for the ten
  supported types); Lean Product / Value Proposition / Business Model where relevant.

## Process
1. Pick the `canvas_type`.
2. For each cell/element, reference the canonical record ids it projects (`refs`).
3. Keep no fact that is not backed by a referenced record.
4. Refresh when the underlying records change.

## Structured output
Canvas records (`schemas/canvas.schema.json`) whose elements each carry `refs`.

## Quality criteria
- Every element references ≥1 real record; no orphan facts; projection stays current.

## Definition of Done
- A canvas that is fully traceable to canonical Product Knowledge.

## Failure modes
- Canvas elements with no backing record (dangling refs — caught by
  `tests/test_canvas_refs.py`).
- Treating the canvas as truth or as a gate.

## Escalation / governance
- Canvases never change canonical truth; they project it. Referential integrity is enforced by
  the tests.
