---
name: technical-investigation
description: (v1 lightweight) Run simple technical spikes to reduce feasibility uncertainty and produce observations as raw material for Evidence. Depth deliberately limited in v1.
---

# Technical Investigation  *(v1: deliberately lightweight)*

> ⚠️ **Deliberate v1 limitation.** This skill has a complete contract but a **shallow process** in
> v1, matching the deliberately lightweight **Engineer** agent
> ([ADR 0011](../../docs/adr/0011-lightweight-designer-engineer.md)). v1 validates reasoning,
> learning and governance — not a software-development lifecycle. The interface is stable so it
> can be expanded later (architecture modelling, automated build/benchmark, security/perf work)
> without changing how Evidence is produced.

## Purpose
Reduce **feasibility / technical-constraint uncertainty** through **simple spikes** — producing
measured observations that can become Evidence.

## When to use
- When a feasibility question blocks a decision and a quick spike can settle it.

## When NOT to use
- For production build/delivery (out of v1 scope).
- When the question is desirability/usability (use `user-research`).

## Inputs
- A Learning Objective; enough context to scope a small spike.

## Definition of Ready
- A specific feasibility question and a bounded spike idea.

## Methodology selection (v1)
- Time-boxed spike / proof-of-concept / benchmark. Keep it minimal and measured.

## Process (v1)
1. Define the spike and the measurement.
2. Run it; capture results/benchmarks as **artifact references** with provenance.
3. Record the **measured observation** (not an opinion about feasibility).
4. Hand observations + provenance to `evidence-appraisal`.

## Structured output
Artifact reference + measured observations with limitations.

## Quality criteria
- Observations are measured, not asserted; scope stayed within the time-box; provenance complete.

## Definition of Done
- An appraisable feasibility observation tied to the Learning Objective.

## Failure modes
- Presenting **LLM confidence about feasibility as Evidence** (it is not).
- Scope creep beyond a small spike.

## Escalation / governance
- If feasibility needs engineering depth beyond v1, escalate rather than over-claim.
