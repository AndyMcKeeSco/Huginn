---
name: opportunity-mapping
description: Organise Opportunities into an Opportunity Solution Tree / Opportunity Space with parent-child structure under target Outcomes.
---

# Opportunity Mapping

## Purpose
Structure discovered Opportunities into a coherent **Opportunity Space** — a Teresa Torres–style
**Opportunity Solution Tree** — so leverage and relationships are visible.

## When to use
- After discovery, to organise candidate Opportunities.
- When the space has grown tangled or overlapping.

## When NOT to use
- To score/choose (use `opportunity-assessment` / `-selection`).
- To attach solutions (the tree's solution branches are out of v1 scope depth).

## Inputs
- Candidate Opportunities; target Outcome(s).

## Definition of Ready
- A set of Opportunities exists, each linked to an Outcome.

## Methodology selection
- **Opportunity Solution Trees** — decompose broad opportunities into specific ones.
- **JTBD** decomposition where a job splits into sub-jobs.

## Process
1. Cluster related Opportunities; identify parents and children.
2. Set `parent_id` to build the hierarchy under each Outcome.
3. Merge duplicates; split overly broad ones; retire non-opportunities.
4. Keep the tree connected to Outcomes.

## Structured output
Updated Opportunity records with hierarchy, plus an **Opportunity Solution Tree canvas**
projection.

## Quality criteria
- Single connected space per Outcome; no orphans; sensible granularity.

## Definition of Done
- A navigable Opportunity Space the Product Owner can target from.

## Failure modes
- A flat, unstructured list.
- Duplicated or overlapping branches.

## Escalation / governance
- Structuring is not prioritisation; targeting remains the Product Owner's decision.
