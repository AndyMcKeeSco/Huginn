# Escalation Rules

The AI Chief of Staff operates by **Management by Exception**: it does **not** escalate because
something happened; it escalates because a boundary condition is met. This document is the
explicit rule set. The structured output of an escalation (or a considered non-escalation) is a
**Decision Brief** (see [`decision-brief-spec.md`](decision-brief-spec.md)).

## Escalate only when at least one holds

| # | Condition | Why it is human's |
|---|---|---|
| E1 | **Human authority is required** (e.g. a Challenge change / `decide_pivot_reframe`). | Reserved decision. |
| E2 | **Consequence exceeds delegated authority.** | Beyond what an agent may commit. |
| E3 | **Uncertainty cannot be resolved autonomously** (no sufficiently reliable Test will settle it in time). | Judgement call. |
| E4 | **Governance requires intervention** (an attempted breach of decision rights). | Rule enforcement. |
| E5 | **Agent conflict cannot be resolved** (material, standing disagreement between agents). | Needs an arbiter. |
| E6 | **Strategic assumptions may no longer hold** (a strong Product Scout signal invalidating a load-bearing Proposition). | Direction risk. |

## Exception conditions the ACoS watches for

The ACoS continuously observes the other agents and the Product Knowledge for:

- repeated **failed Tests** on the same uncertainty;
- **stalled** Tests / work;
- **unresolved high-consequence uncertainty**;
- **major contradictory Learning**;
- **significant unexpected Outcome movement** (good or bad);
- a **major new Product Scout signal**;
- a **material governance violation**;
- a **Product Owner Pivot/Reframe Recommendation**;
- the autonomous system's **inability to make justified progress**.

A condition being present triggers *assessment*, not automatic escalation. The ACoS aggregates
related issues, prioritises, and decides whether a boundary condition (E1–E6) is actually met.

## Aggregation and noise control

- **Aggregate** related exceptions into one brief rather than many.
- **Prioritise** by urgency × consequence.
- **Prepare a concise brief**, not a dump of raw agent activity.
- Record a **no-escalation** decision (with rationale) when routine handling suffices — this is
  a first-class output, not silence. It is how the ACoS demonstrates it is *managing* attention.

## What escalation is never used for

- Routine autonomous activity that is within delegated authority.
- Micromanaging individual agents.
- Becoming an alternative source of Product Knowledge.

## Worked scenarios

Two end-to-end examples live in the worked example:

- **No escalation necessary** — `examples/complaints/briefs/DB-01-no-escalation.yaml`.
- **Human Decision Brief required** — `examples/complaints/briefs/DB-02-escalate.yaml`.
