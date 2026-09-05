# ADR 0007 — Reasoning loop vs operating loop

**Status:** Accepted

## Context
Two different loops are easy to conflate: how *knowledge* is structured/revised, and how *work* is
scheduled over time. Conflating them makes the kernel carry sprint mechanics and makes sprints
carry epistemology.

## Decision
Keep them **separate**:
- **Reasoning kernel** — `Intent → Opportunity → Proposition → Test → Learning ↺`; recursive, not
  a pipeline. Learning may update any earlier part.
- **Operating loop** — `Assess Risk → Sprint Goal → Select Tests → Execute → Capture Evidence →
  Produce Learning → Update Product Knowledge → Learning Accounting → Sprint Outcome →
  Pivot/Persevere → Next Sprint`.

## Consequences
- You can reason about Intent→…→Learning without sprint mechanics, and run sprints without
  collapsing them into the kernel.
- Documented in `docs/methodology/reasoning-kernel.md` and
  `docs/operating-model/operating-loop.md`.
