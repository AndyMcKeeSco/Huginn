---
name: evidence-appraisal
description: Appraise raw material into Evidence records with provenance, method, strength and limitations, enforcing that prototypes and LLM confidence are not Evidence.
---

# Evidence Appraisal

## Purpose
Turn raw material (observations, sources, spike results) into **appraised Evidence** — with
provenance, method, strength and limitations — the only thing Learning may stand on.

## When to use
- After any research modality produces observations.

## When NOT to use
- To synthesise conclusions (use `learning-synthesis`).

## Inputs
- Observations and artifact references from research modalities.

## Definition of Ready
- An observation with a traceable source.

## Methodology selection
- **Critical appraisal / Evidence-Based Practice** for validity, reliability, relevance.
- **Weight of Evidence** to assign strength.

## Process
1. Confirm the observation derives from a real source (not a prototype-as-proof, not LLM
   confidence).
2. Record provenance (source, method, when, conditions).
3. Assess `strength` (weak/moderate/strong) and `limitations`.
4. Link `supports`/`contradicts` to Propositions.

## Structured output
Evidence records (`schemas/evidence.schema.json`).

## Quality criteria
- Provenance complete; strength justified; limitations honest; guardrails enforced.

## Definition of Done
- Evidence ready for synthesis, with over-reach impossible to hide.

## Failure modes
- Admitting a prototype or LLM assertion as Evidence.
- Missing limitations; inflating strength.

## Escalation / governance
- Guardrails: a prototype is not Evidence; LLM confidence is not Evidence; no provenance → no
  Evidence.
