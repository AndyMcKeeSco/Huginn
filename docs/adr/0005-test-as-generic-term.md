# ADR 0005 — "Test" as the generic term (Experiment is a subtype)

**Status:** Accepted

## Context
Not all learning is experimental. Interviews, desk research, data analysis and technical spikes
all reduce uncertainty. Calling everything an "experiment" over-signals rigour and biases toward
costly methods, violating "least costly sufficiently reliable".

## Decision
**Test** is the generic term: *deliberate work undertaken to reduce a specified uncertainty in
order to inform a decision.* **Experiment** is one `method` among many. Every Test must carry a
**Learning Objective** and an **Intended Decision Consequence**.

## Consequences
- `schemas/test.schema.json` requires `learning_objective`, `intended_decision_consequence`,
  `evidence_sought`, `method` and a `target`; `method` is an enum including `experiment`.
- `tests/test_test_requirements.py` enforces the required fields.
- Encourages choosing the cheapest sufficiently reliable method.
