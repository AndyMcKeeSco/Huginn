"""Governance invariants, enforced from governance/decision_rights.yaml and the schemas."""
import copy

import pytest

import governance as gov
import huginn_pk as pk


# --- Decision-rights table (single source of truth) ---------------------------------------

def test_only_human_may_change_challenge():
    assert gov.allowed_actors("change_challenge") == ["human"]
    for agent in [
        "product-owner",
        "designer",
        "engineer",
        "proposition-steward",
        "research-orchestrator",
        "learning-steward",
        "product-scout",
        "ai-chief-of-staff",
    ]:
        assert not gov.may(agent, "change_challenge"), f"{agent} must not change the Challenge"


def test_only_product_owner_originates_pivot_reframe():
    assert gov.may("product-owner", "originate_pivot_reframe")
    for agent in ["ai-chief-of-staff", "research-orchestrator", "product-scout", "learning-steward"]:
        assert not gov.may(agent, "originate_pivot_reframe")


def test_ai_chief_of_staff_is_boundaried():
    """The ACoS manages attention/governance, not product truth."""
    for action in [
        "change_challenge",
        "originate_pivot_reframe",
        "select_target_opportunity",
        "propose_sprint_goal",
        "revise_belief",
        "admit_canonical_learning",
    ]:
        assert not gov.may("ai-chief-of-staff", action), f"ACoS must not perform {action}"


def test_ai_chief_of_staff_may_escalate_and_brief():
    assert gov.may("ai-chief-of-staff", "author_decision_brief")
    assert gov.may("ai-chief-of-staff", "escalate_to_human")


def test_only_learning_steward_admits_canonical_learning():
    assert gov.allowed_actors("admit_canonical_learning") == ["learning-steward"]


def test_check_action_raises_for_forbidden():
    with pytest.raises(PermissionError):
        gov.check_action("ai-chief-of-staff", "change_challenge")


# --- Schema-level governance --------------------------------------------------------------

PRR = {
    "id": "PRR-1",
    "kind": "pivot_reframe_recommendation",
    "originating_agent": "product-owner",
    "recommendation": "Reconsider whether the Outcome should target routing rather than tone.",
    "scope": "outcome",
    "evidence_basis": ["LRN-1"],
    "provenance": {"created_by": "product-owner"},
}


def test_valid_pivot_reframe_recommendation():
    assert pk.is_valid(PRR)


def test_pivot_reframe_must_originate_with_product_owner():
    bad = copy.deepcopy(PRR)
    bad["originating_agent"] = "ai-chief-of-staff"
    assert not pk.is_valid(bad), "an ACoS-originated Pivot/Reframe Recommendation must fail schema validation"


DECISION_BRIEF = {
    "id": "DB-1",
    "kind": "decision_brief",
    "authored_by": "ai-chief-of-staff",
    "escalate": False,
    "trigger": "routine_activity",
    "what_happened": "A test completed as planned.",
    "why_it_matters": "Within delegated authority; no reserved decision engaged.",
    "no_escalation_rationale": "Outcome unaffected; belief update handled by the Proposition Steward.",
    "provenance": {"created_by": "ai-chief-of-staff"},
}


def test_valid_no_escalation_brief():
    assert pk.is_valid(DECISION_BRIEF)


def test_decision_brief_must_be_authored_by_acos():
    bad = copy.deepcopy(DECISION_BRIEF)
    bad["authored_by"] = "product-owner"
    assert not pk.is_valid(bad), "only the AI Chief of Staff may author a Decision Brief"


def test_no_escalation_brief_requires_rationale():
    bad = copy.deepcopy(DECISION_BRIEF)
    del bad["no_escalation_rationale"]
    assert not pk.is_valid(bad), "a no-escalation brief must record why routine handling is sufficient"


def test_escalating_brief_requires_decision_fields():
    bad = copy.deepcopy(DECISION_BRIEF)
    bad["escalate"] = True
    bad["trigger"] = "pivot_reframe_recommendation"
    del bad["no_escalation_rationale"]
    # escalate=true now requires decision_required, urgency, decision_authority, options
    assert not pk.is_valid(bad), "an escalating brief must state the decision, urgency, authority and options"
