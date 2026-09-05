# Challenge Governance

The **Challenge** is the top of the Intent hierarchy — the strategic problem or ambition Huginn
is organised around. It is the one part of the product model that is **human-reserved**
(see [ADR 0016](../adr/0016-human-governed-challenge.md)).

## The rule

> **No agent may change the Challenge.** Only a human may.

This is enforced three ways:

1. `schemas/intent.schema.json` requires a Challenge to be `human_governed: true` and to have no
   parent.
2. `governance/decision_rights.yaml` sets `change_challenge.allowed_actors: [human]`.
3. `tests/test_governance.py::test_only_human_may_change_challenge` asserts no agent may.

## The only route from an agent to a Challenge change

An agent cannot change the Challenge, but the **Product Owner** — and only the Product Owner —
may **recommend** that a human reconsider it, via a **Pivot/Reframe Recommendation**
(`schemas/pivot-reframe-recommendation.schema.json`, `scope: challenge`).

```
Product Owner  ──originates──▶  Pivot/Reframe Recommendation (scope: challenge)
                                        │
                          AI Chief of Staff prepares a Decision Brief
                                        │
                                   Human decides
                              (accept / reject / defer)
```

At no point does an agent enact the change. The recommendation is evidence-based (it must cite
Learning), the AI Chief of Staff routes it to a human with a Decision Brief, and the human holds
`decide_pivot_reframe` authority.

## What the AI Chief of Staff must **not** do

The AI Chief of Staff manages attention and governance, not product truth. It must not:

- change Intent or the Challenge;
- originate a Pivot/Reframe Recommendation;
- make decisions reserved to the Product Owner.

These prohibitions are asserted by `tests/test_governance.py::test_ai_chief_of_staff_is_boundaried`.

## Why reserve the Challenge

The Challenge encodes strategic intent that carries consequences beyond what the autonomous
system can be accountable for. Reserving it keeps humans in authority over *direction* while
letting Huginn move fast on *learning*. Everything below the Challenge — Impacts, Outcomes,
Opportunities, Propositions, Tests — is where the autonomous system does its work.
