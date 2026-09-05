---
name: proposition-linking
description: Establish relationships between Propositions and to Opportunities/Solutions (supports, depends-on, contradicts, refines) to build an argument structure.
---

# Proposition Linking

## Purpose
Connect Propositions to each other and to Opportunities/Solutions so Huginn has an **argument
structure**, not a bag of beliefs — enabling dependency-aware belief revision and risk analysis.

## When to use
- After forming/classifying Propositions.
- When a new Proposition relates to existing ones.

## When NOT to use
- To detect contradictions specifically (use `contradiction-detection`).

## Inputs
- The Proposition set; related Opportunities/Solutions.

## Definition of Ready
- At least two Propositions, or a Proposition plus a related entity.

## Methodology selection
- **Toulmin argumentation / argument & causal mapping** to express warrant and dependency.
- Relationship types: `supports`, `depends_on`, `contradicts`, `refines`, `relates_to`.

## Process
1. For each Proposition, identify what it supports/depends-on/refines.
2. Add `relationships` entries with correct type and target id.
3. Note load-bearing dependencies for the Product Owner's risk view.

## Structured output
Updated Proposition `relationships`; an argument/dependency view feeding `risk-assessment`.

## Quality criteria
- Relationship types are accurate; no dangling targets.

## Definition of Done
- Dependencies explicit enough to propagate belief revision.

## Failure modes
- Over-linking (noise) or under-linking (hidden dependencies).
- Mislabelling a contradiction as `relates_to`.

## Escalation / governance
- Linking is internal to the belief model; it does not change priority or Intent.
