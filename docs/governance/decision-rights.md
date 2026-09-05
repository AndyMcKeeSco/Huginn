# Decision Rights

Huginn separates **who is responsible** (agents), **what capability is used** (skills) and
**who is permitted to decide** (decision rights). This document explains the decision-rights
model; the machine-readable, enforced source of truth is
[`governance/decision_rights.yaml`](../../governance/decision_rights.yaml), which the tests in
`tests/test_governance.py` assert against.

## Principle

Autonomy is delegated, not assumed. Each agent may act within its delegated authority; anything
beyond it is **reserved** — most importantly, changes to the strategic **Challenge**, which are
reserved to a human.

## The table

| Action | Allowed actors | Notes |
|---|---|---|
| `change_challenge` | **human** | No agent may change the Challenge. |
| `change_impact` | product-owner, human | PO owns Impact within governance. |
| `change_outcome` | product-owner, human | Outcomes are measurable; PO owns them. |
| `select_target_opportunity` | product-owner | Sets `role: target`. |
| `prioritise` | product-owner | Opportunities / work / Tests. |
| `propose_sprint_goal` | product-owner | Trio agrees; PO proposes. |
| `originate_pivot_reframe` | **product-owner** | Only the PO may originate a Pivot/Reframe Recommendation. |
| `decide_pivot_reframe` | **human** | Especially a Challenge reframe. |
| `introduce_signal` | product-scout | External signals. |
| `introduce_candidate_opportunity` | product-scout, product-owner | Candidate ≠ adopted. |
| `introduce_candidate_proposition` | product-scout, proposition-steward, product-owner | |
| `revise_belief` | proposition-steward | Confidence / epistemic state. |
| `design_test` | research-orchestrator, product-owner | Convert priorities into Tests. |
| `admit_canonical_learning` | **learning-steward** | Admission control. |
| `author_decision_brief` | **ai-chief-of-staff** | At the human/autonomy boundary. |
| `escalate_to_human` | **ai-chief-of-staff** | Management by Exception. |

## Reserved vs delegated

- **Reserved (human):** `change_challenge`, `decide_pivot_reframe`.
- **Delegated (agent, within scope):** everything else, subject to the allowed-actors list.

A **Decision** record (`schemas/decision.schema.json`) captures the `authority` under which it
was made (`delegated` or `reserved_human`), so every consequential decision is auditable.

## How this is enforced

1. **Schema-level** — e.g. `pivot-reframe-recommendation.schema.json` fixes
   `originating_agent` to `product-owner`; `decision-brief.schema.json` fixes `authored_by` to
   `ai-chief-of-staff`; `intent.schema.json` requires a Challenge to be `human_governed`.
2. **Rule-level** — `governance/decision_rights.yaml` + `scripts/governance.py` answer
   "may `<actor>` perform `<action>`?"
3. **Test-level** — `tests/test_governance.py` asserts the invariants (challenge is
   human-only; only the PO originates a Pivot/Reframe; the ACoS is boundaried).

See also [`challenge-governance.md`](challenge-governance.md) and
[`escalation-rules.md`](escalation-rules.md).
