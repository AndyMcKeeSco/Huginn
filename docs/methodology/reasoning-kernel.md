# The Reasoning Kernel

Huginn's reasoning is deliberately small. It has **five entities** and one loop:

```
INTENT → OPPORTUNITY → PROPOSITION → TEST → LEARNING ↺
```

The arrow is a *typical* flow, not a strict pipeline. The loop is **recursive**: a Learning may
update any earlier part of the model — a Proposition's confidence, the choice of Target
Opportunity, even (via the governed route) the Intent.

Keeping the kernel small is a design decision (see
[ADR 0001](../adr/0001-five-entity-reasoning-kernel.md)). Everything else in Huginn — risk,
evidence, decisions, sprints, canvases — is *supporting machinery* arranged around these five.

## Why these five

| Entity | Answers | One-line rule |
|---|---|---|
| **Intent** | What are we trying to achieve? | Typed hierarchy Challenge → Impact → Outcome; Challenge is human-governed. |
| **Opportunity** | Where might there be leverage? | A need/pain/desire/problem — **not** a Solution. |
| **Proposition** | What do we believe, suspect, or need to establish? | One superclass: Claim \| Assumption \| Hypothesis. |
| **Test** | What should we do to reduce this uncertainty? | Must have a Learning Objective **and** an Intended Decision Consequence. |
| **Learning** | What did the Evidence teach us, and what does it change? | Must never exceed what its Evidence supports. |

See [`entities.md`](entities.md) for the full definition of each, and `schemas/` for the
machine-operable form.

## What is deliberately *not* in the kernel

- **Risk** is not a sixth entity. It is a **continuous assessment** across the whole model,
  owned by the Product Owner. Risk determines *attention*, not structure. See
  [`risk.md`](risk.md) and [ADR 0006](../adr/0006-risk-as-assessment.md).
- **Evidence** is a *supporting concept* that feeds Learning, not a kernel entity. See
  [`evidence.md`](evidence.md).
- **Solutions, Decisions, Sprints, Canvases** are all supporting records, not kernel entities.

## Recursion, not pipeline

A Learning can propagate backwards:

- *Learning → Proposition* — revise confidence / epistemic state (Proposition Steward).
- *Learning → Opportunity* — resize, merge, split, or de-prioritise an Opportunity.
- *Learning → Intent* — evidence that an Outcome is mis-specified, or (via the governed route
  only) that the Challenge should be reframed → a **Pivot/Reframe Recommendation** from the
  Product Owner.
- *Learning → Solution / Decision / risk assessment* — update downstream records.

This backward flow is the whole point: Huginn is a *learning* system, so new Learning is
allowed to change what came before it — under governance.

## The kernel vs the operating loop

The **reasoning kernel** (this document) describes *how knowledge is structured and revised*.
The **operating loop** (`../operating-model/operating-loop.md`) describes *how work is
scheduled over time* in sprints. They are intentionally separate (ADR 0007): you can reason
about Intent→…→Learning without reference to sprints, and you can run the sprint cadence
without collapsing it into the reasoning model.

## Traceability

Every canonical record carries provenance and relationships, so the chain is always
reconstructable:

```
Intent → Opportunity → Proposition → Test → Evidence → Learning → (Product Knowledge update)
```

This traceability is what lets the Learning Steward guarantee that Learning does not exceed
Evidence, and lets the AI Chief of Staff build Decision Briefs that are concise but fully
traceable back to canonical Product Knowledge.
