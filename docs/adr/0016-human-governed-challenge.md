# ADR 0016 — Human-governed Challenge

**Status:** Accepted

## Context
An autonomous product system that could redefine its own strategic Challenge would be accountable
for consequences beyond what it should decide alone. Humans must retain authority over strategic
direction.

## Decision
The **Challenge** (top of the Intent hierarchy) is **human-governed**: **no agent may change it.**
The only route from an agent to a Challenge change is a **Pivot/Reframe Recommendation**,
**originated solely by the Product Owner**, routed to a human by the AI Chief of Staff via a
Decision Brief; **only a human decides**. The Product Owner must not approve its own strategic
Challenge change.

## Consequences
- Schema-enforced: a Challenge must be `human_governed: true` (`intent.schema.json`);
  `pivot-reframe-recommendation.schema.json` fixes `originating_agent: product-owner`.
- Rule-enforced: `change_challenge.allowed_actors: [human]`;
  `originate_pivot_reframe: [product-owner]` in `governance/decision_rights.yaml`.
- Test-enforced: `tests/test_governance.py` (challenge is human-only; only the PO originates a
  Pivot/Reframe; the ACoS cannot do either).
- See `docs/governance/challenge-governance.md`.
