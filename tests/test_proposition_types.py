"""Proposition superclass: only claim | assumption | hypothesis are valid types."""
import copy

import pytest

import huginn_pk as pk

BASE = {
    "id": "PROP-1",
    "kind": "proposition",
    "type": "assumption",
    "statement": "Complainants know which organisation is responsible for their complaint.",
    "epistemic_state": "open",
    "confidence": 0.4,
    "provenance": {"created_by": "proposition-steward"},
}


@pytest.mark.parametrize("ptype", ["claim", "assumption", "hypothesis"])
def test_supported_types_are_valid(ptype):
    rec = copy.deepcopy(BASE)
    rec["type"] = ptype
    assert pk.is_valid(rec)


def test_unsupported_type_fails():
    rec = copy.deepcopy(BASE)
    rec["type"] = "belief"  # not a Proposition type
    assert not pk.is_valid(rec), "an unsupported Proposition type must fail validation"


def test_missing_epistemic_state_fails():
    rec = copy.deepcopy(BASE)
    del rec["epistemic_state"]
    assert not pk.is_valid(rec)
