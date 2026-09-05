# The Operating Loop

The operating loop is **distinct from the reasoning kernel** (see
[ADR 0007](../adr/0007-reasoning-loop-vs-operating-loop.md)). The kernel describes how knowledge
is structured and revised; the operating loop describes how work is scheduled over time.

```
Assess Risk
  → Set Sprint Goal
    → Select Tests/work
      → Execute
        → Capture Evidence
          → Produce Learning
            → Update Product Knowledge
              → Learning Accounting
                → Sprint Outcome
                  → Pivot/Persevere
                    → Next Sprint ↺
```

There is **one shared Product Trio Sprint** (see [`sprint-model.md`](sprint-model.md)).

## Steps

| Step | Owner (lead) | What happens |
|---|---|---|
| **Assess Risk** | Product Owner | Identify the most consequential uncertainty between us and the Outcome. |
| **Set Sprint Goal** | Product Owner (proposes) | A goal framed as reducing that uncertainty / moving that Outcome. Trio agrees. |
| **Select Tests/work** | Research Orchestrator (with Trio) | Choose the least costly sufficiently reliable Tests; confirm readiness. |
| **Execute** | Trio + specialists | Run the Tests / do the work across research modalities. |
| **Capture Evidence** | Learning Steward | Appraise raw material into Evidence with provenance. |
| **Produce Learning** | Learning Steward | Synthesise Evidence into Learning that does not exceed it. |
| **Update Product Knowledge** | Proposition Steward + Learning Steward | Revise beliefs, opportunities, intent, solutions, risk. |
| **Learning Accounting** | Product Owner | Account for uncertainty reduced and Outcome movement (see [`learning-accounting.md`](learning-accounting.md)). |
| **Sprint Outcome** | Product Owner | Record what the sprint achieved against its Learning Goals. |
| **Pivot/Persevere** | Product Owner | Decide/recommend: persevere, adjust, or (governed) Pivot/Reframe. |

## The AI Chief of Staff runs alongside, not inside

The AI Chief of Staff is **not a step** in the loop. It observes the loop continuously and, by
**Management by Exception**, decides when a human must be involved (a stalled or repeatedly
failing Test, a high-consequence unresolved uncertainty, a governance breach, a Product Owner
Pivot/Reframe Recommendation). See [`../governance/escalation-rules.md`](../governance/escalation-rules.md).

## What "done" means for a sprint

A sprint is not "done" because work happened. It is done when it can honestly answer:

- Which consequential uncertainty did we reduce, and by how much (with Evidence)?
- Did the target Outcome move, or did we learn why it will not?
- What does the updated Product Knowledge now say, and what did that change?

That honest answer is the input to Pivot/Persevere.
