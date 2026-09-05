"""Governance checks driven by the single source of truth `governance/decision_rights.yaml`.

Both the AI Chief of Staff charter and the test suite reference these rules, so decision
rights have exactly one definition. This module answers: "may <actor> perform <action>?"
"""
from __future__ import annotations

import pathlib
from functools import lru_cache

import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DECISION_RIGHTS = REPO_ROOT / "governance" / "decision_rights.yaml"


@lru_cache(maxsize=1)
def load_decision_rights() -> dict:
    return yaml.safe_load(DECISION_RIGHTS.read_text(encoding="utf-8"))


def actions() -> dict:
    return load_decision_rights()["actions"]


class UnknownAction(KeyError):
    pass


def allowed_actors(action: str) -> list[str]:
    table = actions()
    if action not in table:
        raise UnknownAction(action)
    return list(table[action]["allowed_actors"])


def may(actor: str, action: str) -> bool:
    """True iff `actor` is permitted to perform `action` under the decision-rights table."""
    return actor in allowed_actors(action)


def check_action(actor: str, action: str) -> None:
    """Raise PermissionError if the actor may not perform the action."""
    if not may(actor, action):
        raise PermissionError(
            f"{actor!r} may not perform {action!r}; allowed: {allowed_actors(action)}"
        )
