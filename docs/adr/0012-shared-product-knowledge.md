# ADR 0012 — Shared, canonical Product Knowledge

**Status:** Accepted

## Context
If each agent held its own private state, beliefs would fragment, provenance would break, and the
system could not be governed or audited. "Knowledge survives the agent" requires a canonical store.

## Decision
All agents operate against **shared, canonical Product Knowledge** expressed as **YAML/JSON records
validated by JSON Schema** (`schemas/`), with **stable ids**, **many-to-many relationships** and
**full provenance**. Typical traceability:
`Intent → Opportunity → Proposition → Test → Evidence → Learning`, and Learning may update
Propositions, Opportunities, Intent, Solutions, risk assessments and Decisions.

## Consequences
- One source of truth; agents are stewards, not owners, of the knowledge.
- Provenance and relationships make the whole chain auditable and canvas-projectable.
- `scripts/validate.py` + `tests/` keep records well-formed.
- See `docs/architecture/shared-product-knowledge.md`.
