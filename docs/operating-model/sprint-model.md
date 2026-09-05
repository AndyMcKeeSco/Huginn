# The Sprint Model

There is **one shared Product Trio Sprint**. The Product Owner, Designer and Engineer work the
same sprint toward the intended Outcomes; specialist agents (Proposition Steward, Research
Orchestrator, Learning Steward, Product Scout) participate as their responsibilities require.

## A Sprint carries

| Field | Meaning |
|---|---|
| **Sprint Goal** | Proposed by the Product Owner; framed as reducing consequential uncertainty. |
| **Target Outcome** | The Outcome this sprint is trying to move. |
| **Target Opportunity** | The Opportunity in focus (a `role: target` on an Opportunity). |
| **Consequential uncertainty / risk** | The most consequential uncertainty this sprint addresses. |
| **Learning Goals** | What we intend to learn. |
| **Tests / work** | The Tests selected (least costly sufficiently reliable). |
| **Intended Decision Consequences** | For each Test: what we will do given what we learn. |

Schema: [`schemas/sprint.schema.json`](../../schemas/sprint.schema.json).

## Roles in the sprint

- **Product Owner** proposes the Sprint Goal, owns risk and prioritisation, runs Learning
  Accounting and the Pivot/Persevere Review.
- **Designer** participates where design is relevant (usability/desirability uncertainty,
  lightweight prototypes). *v1: intentionally lightweight.*
- **Engineer** participates where technical questions are relevant (feasibility, constraints,
  simple spikes). *v1: intentionally lightweight.*
- **Research Orchestrator** turns Learning Goals into ready, sequenced Tests and manages flow.
- **Proposition Steward** and **Learning Steward** keep beliefs and canonical Learning honest.
- **Product Scout** feeds in external signals that may change what matters.
- **AI Chief of Staff** watches for exceptions and manages human attention.

## Sprint Outcome

At sprint end, the Product Owner records a **Sprint Outcome**
([`schemas/sprint-outcome.schema.json`](../../schemas/sprint-outcome.schema.json)): what was
learned, which uncertainty was reduced and by how much, whether the target Outcome moved, and the
Pivot/Persevere decision or recommendation.

## Pivot/Persevere

Every sprint ends with an explicit **Pivot/Persevere Review**
([`schemas/pivot-persevere-review.schema.json`](../../schemas/pivot-persevere-review.schema.json)).
Options: **persevere**, **adjust within the current frame**, or — only via the Product Owner and
only through a **Pivot/Reframe Recommendation** to a human — **pivot/reframe the Challenge**. The
Challenge itself is never changed autonomously.
