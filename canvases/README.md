# Canvases

Canvases are **human-readable projections of Product Knowledge**. They are **not** canonical
truth and **not** lifecycle gates (see [ADR 0014](../docs/adr/0014-canvases-as-projections.md)).
Every canvas element references canonical records by id, so a canvas can always be regenerated
from — and traced back to — the underlying Product Knowledge.

- **Schema:** [`schemas/canvas.schema.json`](../schemas/canvas.schema.json)
- **Generic template:** [`templates/canvas.template.yaml`](../templates/canvas.template.yaml)
- **Skill that maintains them:** [`skills/canvas-management`](../skills/canvas-management/SKILL.md)
- **Referential integrity is enforced by:** [`tests/test_canvas_refs.py`](../tests/test_canvas_refs.py)
- **Worked instances:** [`examples/complaints/canvases/`](../examples/complaints/canvases/)

## Rules

1. A canvas **projects** canonical records; it never originates truth.
2. Every element carries `refs: [<canonical id>, ...]` — no orphan facts.
3. Canvases are regenerated when the records they project change.
4. Nothing gates on a canvas; gates live in governance and the operating loop.

## The ten supported canvas types

| `canvas_type` | Projects | Primary audience |
|---|---|---|
| `intent_outcomes` | Challenge → Impact → Outcome hierarchy | Leadership, Trio |
| `opportunity_solution_tree` | Opportunity Space under an Outcome | Trio |
| `propositions_assumptions` | Claims/Assumptions/Hypotheses + epistemic state | Trio, Proposition Steward |
| `risk_confidence` | Ranked consequential uncertainty + confidence | Product Owner, ACoS |
| `sprint_learning_history` | Sprints, Learnings, Pivot/Persevere over time | Trio, leadership |
| `value_proposition` | User jobs/pains/gains vs offering | Trio |
| `product_model` | How the product creates the Outcome | Trio |
| `business_model` | How value is captured/sustained | Leadership |
| `feasibility_constraints` | Technical constraints & feasibility uncertainty | Engineer, Product Owner |
| `lean_product` | Problem/solution/MVP/metrics (Lean Product Canvas) | Trio |

## Authoring a canvas

Use the `canvas-management` skill. Pick a `canvas_type`, then for each cell add an element whose
`refs` point at the canonical records it shows. Example (Intent/Outcomes):

```yaml
id: CNV-intent-01
kind: canvas
canvas_type: intent_outcomes
title: "Complaints — Intent & Outcomes"
projection_of: product_knowledge
elements:
  - cell: challenge
    refs: [INT-challenge-complaints]
  - cell: outcome
    label: "Correct first-time routing"
    refs: [INT-outcome-first-time-routing]
provenance:
  created_by: product-owner
```

Because the elements only reference ids, the canvas cannot drift from the truth it projects —
if a referenced record is retired or changed, the canvas is refreshed, not silently left stale.
