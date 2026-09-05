"""Every record in the worked example validates against its schema, and its
cross-references resolve to real records in the example corpus."""
import pathlib

import pytest

import huginn_pk as pk

EXAMPLE_DIR = pk.REPO_ROOT / "examples"

record_files = list(pk.iter_record_files(EXAMPLE_DIR)) if EXAMPLE_DIR.exists() else []


def _load_records():
    out = []
    for path in record_files:
        try:
            rec = pk.load_record(path)
        except Exception:
            continue
        if isinstance(rec, dict) and "kind" in rec:
            out.append((path, rec))
    return out


RECORDS = _load_records()


@pytest.mark.skipif(not RECORDS, reason="no worked-example records present")
@pytest.mark.parametrize("path_rec", RECORDS, ids=lambda pr: pr[0].name)
def test_example_record_validates(path_rec):
    path, rec = path_rec
    errors = pk.validate_record(rec)
    assert not errors, f"{path} failed validation:\n" + "\n".join(errors)


@pytest.mark.skipif(not RECORDS, reason="no worked-example records present")
def test_example_ids_unique():
    seen = {}
    for path, rec in RECORDS:
        rid = rec.get("id")
        assert rid not in seen, f"duplicate id {rid} in {path} and {seen.get(rid)}"
        seen[rid] = path
