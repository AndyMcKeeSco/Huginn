# Designer — Interfaces (stable contract for later expansion)

The Designer is lightweight in v1, but its **interfaces are stable** so a much richer Designer can
be dropped in later without changing the reasoning kernel or the other agents. Expansion means
deepening the *behind-the-interface* behaviour, not changing these contracts.

## Inbound requests (what the Designer accepts)

| Request | From | Payload | v1 behaviour |
|---|---|---|---|
| `assess_design_uncertainty` | Product Owner | Target Opportunity + Propositions | Return a short list of usability/desirability uncertainties with rough consequence. |
| `propose_design_activity` | Product Owner / Research Orchestrator | a Learning Objective | Propose a simple, cheap activity (sketch, lightweight prototype, design critique). |
| `produce_prototype` | Research Orchestrator | activity spec | Create/coordinate a lightweight prototype; register it as an **artifact reference**. |
| `advise_design_implications` | Product Owner | a decision/option | Return plain-language design implications. |

## Outbound products (what the Designer emits)

| Product | Schema | Notes |
|---|---|---|
| Artifact reference | `schemas/artifact-ref.schema.json` | A prototype/design is an artifact, **not** Evidence. |
| Observation of prototype interaction | feeds `schemas/evidence.schema.json` (via Learning Steward) | Only *observed interaction* becomes Evidence. |
| Design-uncertainty note | Decision input to the Product Owner | Not canonical truth. |

## Invariants that must survive expansion

1. A prototype/design is an **artifact reference**, never Evidence.
2. The Designer never admits Learning (Learning Steward) or sets priority (Product Owner).
3. The Designer contributes to Tests but does not bypass the Test contract (Learning Objective +
   Intended Decision Consequence).
4. All Designer output is traceable via provenance.

## Expansion roadmap (non-binding)

Later versions may add: a real design skill library, higher-fidelity prototyping, design-system
stewardship, generative design exploration, and autonomous usability evaluation — all **behind
the interfaces above**.
