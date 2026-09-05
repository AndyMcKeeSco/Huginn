"""Huginn Product Knowledge helpers: schema loading, validation, and record IO.

Shared by the validation CLI (`validate.py`), the scaffolder (`new_record.py`) and the
test suite (`tests/`). Pure-Python; depends only on `jsonschema` (>=4.18, for `referencing`)
and `pyyaml`.
"""
from __future__ import annotations

import json
import pathlib
from functools import lru_cache

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "schemas"
TEMPLATE_DIR = REPO_ROOT / "templates"

# A record's `kind` field selects which schema validates it.
KIND_TO_SCHEMA = {
    "intent": "intent.schema.json",
    "opportunity": "opportunity.schema.json",
    "proposition": "proposition.schema.json",
    "test": "test.schema.json",
    "evidence": "evidence.schema.json",
    "learning": "learning.schema.json",
    "solution": "solution.schema.json",
    "decision": "decision.schema.json",
    "sprint": "sprint.schema.json",
    "sprint_outcome": "sprint-outcome.schema.json",
    "pivot_persevere_review": "pivot-persevere-review.schema.json",
    "pivot_reframe_recommendation": "pivot-reframe-recommendation.schema.json",
    "artifact_ref": "artifact-ref.schema.json",
    "signal": "signal.schema.json",
    "canvas": "canvas.schema.json",
    "decision_brief": "decision-brief.schema.json",
}


def schema_files() -> list[pathlib.Path]:
    return sorted(SCHEMA_DIR.glob("*.json"))


@lru_cache(maxsize=1)
def registry() -> Registry:
    """A referencing Registry holding every schema under its own $id, so relative
    cross-refs (e.g. `common.defs.json#/$defs/...`) resolve against the base $id."""
    resources = []
    for path in schema_files():
        contents = json.loads(path.read_text(encoding="utf-8"))
        uri = contents["$id"]
        resources.append((uri, Resource.from_contents(contents)))
    return Registry().with_resources(resources)


@lru_cache(maxsize=None)
def _schema_contents(filename: str) -> dict:
    return json.loads((SCHEMA_DIR / filename).read_text(encoding="utf-8"))


def validator_for_kind(kind: str) -> Draft202012Validator:
    if kind not in KIND_TO_SCHEMA:
        raise KeyError(f"Unknown record kind: {kind!r}. Known kinds: {sorted(KIND_TO_SCHEMA)}")
    schema = _schema_contents(KIND_TO_SCHEMA[kind])
    return Draft202012Validator(schema, registry=registry())


def validate_record(record: dict) -> list[str]:
    """Validate one record by its `kind`. Returns a list of human-readable error strings."""
    if not isinstance(record, dict):
        return ["record is not a mapping/object"]
    kind = record.get("kind")
    if kind is None:
        return ["record has no `kind` field, so no schema can be selected"]
    try:
        validator = validator_for_kind(kind)
    except KeyError as exc:
        return [str(exc)]
    errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
    return [f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in errors]


def is_valid(record: dict) -> bool:
    return not validate_record(record)


def load_yaml(path: pathlib.Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def iter_record_files(root: pathlib.Path):
    """Yield every .yaml/.yml/.json record file under `root`."""
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() in {".yaml", ".yml", ".json"} and path.is_file():
            yield path


def load_record(path: pathlib.Path) -> dict:
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    return load_yaml(path)
