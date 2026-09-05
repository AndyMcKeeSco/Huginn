# Core Entities

This document defines the five reasoning-kernel entities in detail. The machine-operable form
of each is in `schemas/`, with blank records in `templates/`.

---

## 1. Intent

**Answers:** "What are we trying to achieve?"

Intent is **hierarchical and typed**:

```
Challenge → Impact → Outcome
```

| Type | Meaning | Governance |
|---|---|---|
| **Challenge** | The strategic problem/ambition we are organised around. | **Human-governed. No agent may change it.** |
| **Impact** | The higher-order effect we expect if we succeed. | Product Owner proposes; governed. |
| **Outcome** | A **measurable behavioural or real-world change**. | Product Owner owns. |

Rules:

- **Outputs/features are not Outcomes.** An Outcome is a change in behaviour or the world, not a
  thing we shipped. (See [ADR 0002](../adr/0002-intent-hierarchy.md).)
- The Challenge is the only strategic anchor a human reserves entirely. Changing it requires a
  **Pivot/Reframe Recommendation** originated by the Product Owner and a human decision.
- Intent forms a tree: one Challenge may have several Impacts; each Impact several Outcomes.

Schema: [`schemas/intent.schema.json`](../../schemas/intent.schema.json).

---

## 2. Opportunity

**Answers:** "Where might there be leverage to achieve the Intent?"

An Opportunity represents a user/customer **need, pain, desire, problem, unmet need, or area of
leverage**.

Rules:

- **Opportunities are not Solutions.** "Users can't find their case reference" is an
  Opportunity; "add a search box" is a Solution.
- Opportunities may form a hierarchy — an **Opportunity Space** / Opportunity Solution Tree
  (Teresa Torres). Larger opportunities decompose into smaller, more specific ones.
- The **Target Opportunity** is normally represented as a *state/role* on an Opportunity (e.g.
  `role: target`) rather than a separate entity, so the tree stays intact as focus shifts.

Schema: [`schemas/opportunity.schema.json`](../../schemas/opportunity.schema.json).

---

## 3. Proposition

**Answers:** "What do we believe, suspect, or need to establish?"

Proposition is a **superclass** with three types (see
[ADR 0003](../adr/0003-proposition-superclass.md)):

| Type | Definition |
|---|---|
| **Claim** | An assertion about the world. |
| **Assumption** | Something that needs to be true for an Opportunity, Solution or decision to succeed. |
| **Hypothesis** | A testable prediction. |

Shared Proposition machinery (identical across all three types):

- stable **ID**
- **statement**
- **type** (`claim` \| `assumption` \| `hypothesis`)
- **epistemic state** (e.g. `open`, `supported`, `contradicted`, `retired`)
- **confidence** (0–1 or a labelled band)
- **supporting Learning** / **contradicting Learning**
- **relationships** (supports, depends-on, contradicts, refines …)
- **provenance**
- **history** (belief-revision trail)

The Proposition Steward owns confidence, epistemic state and belief revision; the specifics live
in [`proposition-steward` charter](../../agents/proposition-steward/CHARTER.md).

Schema: [`schemas/proposition.schema.json`](../../schemas/proposition.schema.json).

---

## 4. Test

**Answers:** "What should we do to reduce this uncertainty?"

A **Test** is *deliberate work undertaken to reduce a specified uncertainty in order to inform a
decision.* "Test" is the generic term (see [ADR 0005](../adr/0005-test-as-generic-term.md)); an
**Experiment** is one Test *method/subtype* among many (interview, analysis, prototype study,
literature review, technical spike …).

Every Test **MUST** include:

1. **Learning Objective** — the specific uncertainty it exists to reduce.
2. **Target Proposition and/or uncertainty** — what it points at.
3. **Evidence sought** — what would count as an observation.
4. **Method** — how the evidence will be gathered.
5. **Intended Decision Consequence** — *"if we learn X we will do Y."* A Test with no decision
   attached to it is not worth running.

Core principle: **use the least costly sufficiently reliable way to learn.** Reliability is a
requirement to be *sufficient for the decision*, not maximised for its own sake.

Schema: [`schemas/test.schema.json`](../../schemas/test.schema.json) — the `learning_objective`
and `intended_decision_consequence` fields are **required**, and the tests in `tests/` enforce
this.

---

## 5. Learning

**Answers:** "What did the Evidence teach us, and what does it change?"

**Learning replaces the term "Finding"** (see [ADR 0004](../adr/0004-learning-replaces-finding.md)).
A Learning is an **evidence-supported statement about what Huginn has learned and its
implications for the product model.**

Learning must include:

- **supporting Evidence** (one or more Evidence records)
- **provenance**
- **limitations** (what it does *not* establish)
- **confidence / strength**
- **implications** (what it changes)
- **affected entities** (Propositions, Opportunities, Intent, Solutions, decisions, risk)

**Cardinal rule: Learning must never exceed what its Evidence supports.** The Learning Steward
enforces this at admission time. A single strong signal is not a general truth; a prototype
reaction is not proof of adoption.

Schema: [`schemas/learning.schema.json`](../../schemas/learning.schema.json) — `evidence` and
`provenance` are **required**.

---

## Relationships at a glance

```
Intent ──has──> Opportunity ──raises──> Proposition ──targeted-by──> Test
                                                             │
                                                        produces
                                                             ▼
                                            Evidence ──supports──> Learning
                                                                     │
                                    updates (any of) ◀──────────────┘
                        Proposition · Opportunity · Intent · Solution · Decision · risk
```

All relationships are many-to-many and carry provenance; see
[`../architecture/shared-product-knowledge.md`](../architecture/shared-product-knowledge.md).
