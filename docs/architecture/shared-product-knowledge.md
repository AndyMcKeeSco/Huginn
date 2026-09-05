# Shared Product Knowledge

(See [ADR 0012](../adr/0012-shared-product-knowledge.md).)

Product Knowledge is Huginn's **single source of truth** — canonical records that all agents read
and write, so that **knowledge survives the agent**.

## Form

- **Records** in YAML/JSON, each with a `kind` and a **stable id** (`PREFIX-slug`).
- **Validated** by JSON Schema Draft 2020-12 (`schemas/`), with a shared `common.defs.json`.
- **Provenance** on every record (who/what created it, when, from which sources, by what method).
- **Relationships** are **many-to-many** (`supports`, `contradicts`, `depends_on`, `refines`,
  `targets`, `derived_from`, …).
- **History** on the entities that revise over time (Propositions, Learnings, Intent).

## Entities and supporting records

Kernel: **Intent, Opportunity, Proposition, Test, Learning**. Supporting: **Evidence, Solution,
Decision, Sprint, Sprint Outcome, Pivot/Persevere Review, Pivot/Reframe Recommendation, Canvas,
Artifact reference, Signal, Decision Brief**. Each has a schema in `schemas/` and a blank record in
`templates/`.

## Traceability

```
Intent → Opportunity → Proposition → Test → Evidence → Learning → (Product Knowledge update)
```

A Learning may update a Proposition, Opportunity, Intent, Solution, risk assessment or Decision —
the loop is recursive (ADR 0007). Because every record carries provenance and relationships, any
conclusion can be traced back to its raw material, and any canvas can be regenerated from the
records it projects (ADR 0014).

## Integrity

- `scripts/validate.py` validates records against schemas (by `kind`).
- `tests/` assert schema validity, intent-hierarchy rules, proposition types, Test requirements,
  Learning-needs-Evidence, governance invariants and canvas referential integrity.
- Admission of canonical **Learning** is controlled by the Learning Steward; belief revision by
  the Proposition Steward — so truth enters the store under discipline, not by assertion.
