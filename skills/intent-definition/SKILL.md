---
name: intent-definition
description: Define and structure Intent as a typed Challenge -> Impact -> Outcome hierarchy, keeping Outcomes measurable and the Challenge human-governed.
---

# Intent Definition

## Purpose
Turn a strategic ambition into a well-formed **Intent** hierarchy: a human-governed **Challenge**,
one or more **Impacts**, and measurable **Outcomes**. Establishes what Huginn is trying to achieve
so all downstream work can be traced to it.

## When to use
- Standing up a new product area, or when Intent is vague, implicit or output-shaped.
- When a human sets or revises the Challenge and the Impact/Outcome structure must be rebuilt.

## When NOT to use
- To change the Challenge autonomously (human-reserved — this skill only *drafts/structures*).
- To define solutions or features (those are not Intent).

## Inputs
- The strategic Challenge statement (from a human).
- Any existing Impacts/Outcomes, context, and constraints.

## Definition of Ready
- A Challenge statement exists and is attributed to a human.
- The intended beneficiaries and rough time horizon are known.

## Methodology selection
- **Impact Mapping** to move from Challenge to Impacts.
- **Outcome-oriented product management** to phrase Outcomes as behavioural/real-world change.
- Use a measure per Outcome (metric, baseline, target, direction, timeframe).

## Process
1. Record the Challenge as `type: challenge`, `human_governed: true`, no parent.
2. Derive Impacts (higher-order effects) as `type: impact` under the Challenge.
3. For each Impact, define Outcomes as `type: outcome` with a `measure`.
4. Sanity-check every Outcome: is it a *change in behaviour or the world*, not an output?
5. Link records and record provenance.

## Structured output
Intent records validating against `schemas/intent.schema.json` (Challenge, Impacts, Outcomes),
plus an Intent/Outcomes canvas projection (`canvas-management`).

## Quality criteria
- Every Outcome has a measure; none is a disguised output/feature.
- The hierarchy is connected (each Impact/Outcome has a parent).
- The Challenge is marked human-governed.

## Definition of Done
- Valid Intent records committed; the Product Owner can trace Opportunities to Outcomes.

## Failure modes
- Outputs masquerading as Outcomes.
- Unmeasurable Outcomes.
- Editing the Challenge without human authority.

## Escalation / governance
- Any change to the Challenge routes to a human (see `docs/governance/challenge-governance.md`).
- Only the Product Owner may change Impacts/Outcomes (`governance/decision_rights.yaml`).
