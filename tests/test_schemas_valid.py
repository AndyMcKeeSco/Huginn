"""Every schema is itself a valid Draft 2020-12 schema, and every template validates."""
import json

import pytest
from jsonschema import Draft202012Validator

import huginn_pk as pk


@pytest.mark.parametrize("schema_path", pk.schema_files(), ids=lambda p: p.name)
def test_schema_is_valid_metaschema(schema_path):
    contents = json.loads(schema_path.read_text(encoding="utf-8"))
    # Raises SchemaError if the schema itself is malformed.
    Draft202012Validator.check_schema(contents)


def test_every_kind_has_a_schema_file():
    for kind, filename in pk.KIND_TO_SCHEMA.items():
        assert (pk.SCHEMA_DIR / filename).exists(), f"missing schema for kind {kind!r}"


TEMPLATES = sorted(pk.TEMPLATE_DIR.glob("*.template.yaml"))


@pytest.mark.parametrize("template_path", TEMPLATES, ids=lambda p: p.name)
def test_template_validates(template_path):
    record = pk.load_yaml(template_path)
    errors = pk.validate_record(record)
    assert not errors, f"{template_path.name} failed validation:\n" + "\n".join(errors)


def test_all_kinds_have_a_template():
    template_kinds = {pk.load_yaml(p).get("kind") for p in TEMPLATES}
    missing = set(pk.KIND_TO_SCHEMA) - template_kinds
    assert not missing, f"kinds without a template: {sorted(missing)}"
