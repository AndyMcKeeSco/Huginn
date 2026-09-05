"""Every Test must have a Learning Objective and an Intended Decision Consequence."""
import copy

import huginn_pk as pk

VALID_TEST = {
    "id": "TEST-1",
    "kind": "test",
    "title": "Card sort of complaint ownership",
    "learning_objective": "Whether complainants can identify the responsible organisation.",
    "target": {"propositions": ["PROP-1"]},
    "evidence_sought": "Accuracy of participants assigning complaints to organisations.",
    "method": "usability_study",
    "intended_decision_consequence": "If accuracy is low we will invest in a routing aid.",
    "provenance": {"created_by": "research-orchestrator"},
}


def test_valid_test():
    assert pk.is_valid(VALID_TEST)


def test_missing_learning_objective_fails():
    bad = copy.deepcopy(VALID_TEST)
    del bad["learning_objective"]
    assert not pk.is_valid(bad), "a Test without a Learning Objective must fail"


def test_missing_intended_decision_consequence_fails():
    bad = copy.deepcopy(VALID_TEST)
    del bad["intended_decision_consequence"]
    assert not pk.is_valid(bad), "a Test without an Intended Decision Consequence must fail"


def test_missing_target_fails():
    bad = copy.deepcopy(VALID_TEST)
    del bad["target"]
    assert not pk.is_valid(bad)


def test_empty_target_fails():
    bad = copy.deepcopy(VALID_TEST)
    bad["target"] = {}
    assert not pk.is_valid(bad), "a Test must target a Proposition and/or an uncertainty"
