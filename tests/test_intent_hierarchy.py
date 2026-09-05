"""Intent hierarchy: Challenge -> Impact -> Outcome typing and rules."""
import copy

import huginn_pk as pk

CHALLENGE = {
    "id": "INT-c1",
    "kind": "intent",
    "type": "challenge",
    "statement": "Reduce customer confusion in a multi-organisation complaints process.",
    "human_governed": True,
    "provenance": {"created_by": "human"},
}

OUTCOME = {
    "id": "INT-o1",
    "kind": "intent",
    "type": "outcome",
    "statement": "More complainants reach the correct organisation first time.",
    "parent_id": "INT-i1",
    "measure": {"metric": "first-contact-correct-routing rate", "direction": "increase"},
    "provenance": {"created_by": "product-owner"},
}


def test_valid_challenge():
    assert pk.is_valid(CHALLENGE)


def test_valid_outcome_with_measure():
    assert pk.is_valid(OUTCOME)


def test_challenge_must_be_human_governed():
    bad = copy.deepcopy(CHALLENGE)
    bad["human_governed"] = False
    assert not pk.is_valid(bad), "a Challenge with human_governed=false must be rejected"


def test_challenge_may_not_have_parent():
    bad = copy.deepcopy(CHALLENGE)
    bad["parent_id"] = "INT-x"
    assert not pk.is_valid(bad), "a Challenge must not have a parent"


def test_outcome_requires_measure():
    """Outputs/features are not Outcomes: an Outcome without a measure is invalid."""
    bad = copy.deepcopy(OUTCOME)
    del bad["measure"]
    assert not pk.is_valid(bad), "an Outcome must be measurable"


def test_impact_and_outcome_require_parent():
    bad = copy.deepcopy(OUTCOME)
    del bad["parent_id"]
    assert not pk.is_valid(bad), "an Outcome must sit under a parent in the hierarchy"
