"""Canonical Learning requires Evidence and provenance, and must not stand on nothing."""
import copy

import huginn_pk as pk

VALID_LEARNING = {
    "id": "LRN-1",
    "kind": "learning",
    "statement": "Most complainants cannot identify the responsible organisation unaided.",
    "evidence": ["EV-1"],
    "limitations": "Single study, 12 participants, one complaint domain.",
    "strength": "moderate",
    "confidence": 0.6,
    "implications": ["Routing help is likely to reduce misdirected complaints."],
    "affected_entities": ["PROP-1"],
    "provenance": {"created_by": "learning-steward"},
}


def test_valid_learning():
    assert pk.is_valid(VALID_LEARNING)


def test_learning_without_evidence_fails():
    bad = copy.deepcopy(VALID_LEARNING)
    del bad["evidence"]
    assert not pk.is_valid(bad), "Learning without Evidence must fail"


def test_learning_with_empty_evidence_fails():
    bad = copy.deepcopy(VALID_LEARNING)
    bad["evidence"] = []
    assert not pk.is_valid(bad), "Learning cannot stand on an empty Evidence list"


def test_learning_without_provenance_fails():
    bad = copy.deepcopy(VALID_LEARNING)
    del bad["provenance"]
    assert not pk.is_valid(bad), "Learning without provenance must fail"


def test_learning_without_limitations_fails():
    bad = copy.deepcopy(VALID_LEARNING)
    del bad["limitations"]
    assert not pk.is_valid(bad), "Learning must state its limitations (bounds the claim)"
