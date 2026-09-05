# Engineer — Interfaces (stable contract for later expansion)

The Engineer is lightweight in v1, but its **interfaces are stable** so a much richer Engineer can
be dropped in later without changing the reasoning kernel or the other agents. Expansion means
deepening the *behind-the-interface* behaviour, not changing these contracts.

## Inbound requests (what the Engineer accepts)

| Request | From | Payload | v1 behaviour |
|---|---|---|---|
| `assess_feasibility_uncertainty` | Product Owner | Target Opportunity + Propositions/Solutions | Return a short list of feasibility/constraint uncertainties with rough consequence. |
| `advise_constraints` | Product Owner / Designer | a proposed direction | Return the technical constraints that bear on it. |
| `run_technical_spike` | Research Orchestrator | a Learning Objective | Run/coordinate a **simple** spike or benchmark; register results as raw material. |
| `advise_engineering_implications` | Product Owner | a decision/option | Return plain-language engineering implications. |

## Outbound products (what the Engineer emits)

| Product | Schema | Notes |
|---|---|---|
| Artifact reference (spike output, benchmark) | `schemas/artifact-ref.schema.json` | Raw material, **not** Evidence. |
| Observation from a spike/benchmark | feeds `schemas/evidence.schema.json` (via Learning Steward) | The measured result — with provenance — is what becomes Evidence. |
| Feasibility note | Decision input to the Product Owner | Not canonical truth. |

## Invariants that must survive expansion

1. LLM confidence about feasibility is **not** Evidence; a measured observation with provenance is.
2. The Engineer never admits Learning (Learning Steward) or sets priority (Product Owner).
3. The Engineer contributes to Tests but does not bypass the Test contract (Learning Objective +
   Intended Decision Consequence).
4. All Engineer output is traceable via provenance.

## Expansion roadmap (non-binding)

Later versions may add: a real engineering skill library, architecture modelling, automated
prototyping/build, CI-driven experiments, performance/security investigation, and delivery
capabilities — all **behind the interfaces above**.
