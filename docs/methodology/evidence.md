# Evidence

Evidence is a **supporting concept**, not one of the five reasoning-kernel entities (see
[ADR 0001](../adr/0001-five-entity-reasoning-kernel.md)). It sits between raw material and
Learning and carries the provenance that makes Learning trustworthy.

## The traceability chain

```
Source / Raw Material → Evidence → Learning → Product Knowledge update
```

- **Source / Raw Material** — the interview recording, the analytics export, the support-ticket
  corpus, the benchmark run, the document. Raw material is *not yet* Evidence.
- **Evidence** — an appraised observation drawn from a source, with provenance, method and
  context attached. Evidence is what a Learning is allowed to stand on.
- **Learning** — the evidence-supported statement of what we now know and what it changes.

## Rules

1. **A prototype is not Evidence.** A prototype is an artifact. *Observed interaction* with a
   prototype (what a user did, said, chose, failed to do) may **produce** Evidence.
2. **LLM confidence is not Evidence.** A model asserting something with high confidence is not an
   observation of the world. It may generate a Proposition to test; it is never itself Evidence.
3. **Evidence requires provenance.** Where it came from, how it was gathered, when, by whom/what,
   and under what conditions. Evidence without provenance cannot support canonical Learning.
4. **Evidence has limitations.** Sample size, selection, recency, method reliability. These
   limitations travel with the Evidence and constrain any Learning built on it.

## Appraisal and triangulation

The **Learning Steward** appraises Evidence (critical appraisal, adapted GRADE principles) and
**triangulates** across independent sources before admitting a Learning into canonical Product
Knowledge. A conclusion supported by one weak source is admitted weakly, if at all; a conclusion
supported by several independent sources of different kinds is admitted more strongly.

## Weight of Evidence

The **Proposition Steward** treats Evidence as *weight for or against* a Proposition and revises
confidence accordingly (Bayesian updating / weight-of-evidence). Contradicting Evidence is
first-class: it is recorded against the Proposition, not discarded.

## Schema

Evidence records are defined in
[`schemas/evidence.schema.json`](../../schemas/evidence.schema.json). Key fields: `id`,
`statement`/`observation`, `source` (raw-material reference and type), `method`, `provenance`,
`limitations`, `strength`, and the `supports`/`contradicts` relationships to Propositions and
Learnings.

Artifacts (prototypes, documents, datasets) are referenced via
[`schemas/artifact-ref.schema.json`](../../schemas/artifact-ref.schema.json) — an artifact
reference is explicitly **not** Evidence; it is a pointer to raw material that Evidence may be
drawn from.
