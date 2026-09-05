"""Canvases are projections: every element must reference canonical Product Knowledge ids,
and (within a corpus) those references must resolve to real records."""
import pathlib

import pytest

import huginn_pk as pk

EXAMPLE_DIR = pk.REPO_ROOT / "examples" / "complaints"


def _canvas(elements):
    return {
        "id": "CNV-x",
        "kind": "canvas",
        "canvas_type": "intent_outcomes",
        "title": "Test canvas",
        "projection_of": "product_knowledge",
        "elements": elements,
        "provenance": {"created_by": "product-owner"},
    }


def test_canvas_element_requires_refs():
    bad = _canvas([{"label": "orphan", "cell": "goal"}])  # no refs
    assert not pk.is_valid(bad), "a canvas element with no canonical refs must fail"


def test_canvas_with_refs_is_valid():
    good = _canvas([{"label": "challenge", "cell": "goal", "refs": ["INT-c1"]}])
    assert pk.is_valid(good)


def _collect_ids_and_canvas_refs(root: pathlib.Path):
    ids: set[str] = set()
    refs: list[tuple[str, str]] = []  # (canvas_id, referenced_id)
    canvases = []
    for path in pk.iter_record_files(root):
        try:
            rec = pk.load_record(path)
        except Exception:
            continue
        if not isinstance(rec, dict) or "id" not in rec:
            continue
        ids.add(rec["id"])
        if rec.get("kind") == "canvas":
            canvases.append(rec)
    for canvas in canvases:
        for element in canvas.get("elements", []):
            for ref in element.get("refs", []):
                refs.append((canvas["id"], ref))
    return ids, refs


@pytest.mark.skipif(not EXAMPLE_DIR.exists(), reason="worked example not present")
def test_worked_example_canvas_refs_resolve():
    ids, refs = _collect_ids_and_canvas_refs(EXAMPLE_DIR)
    dangling = [(cid, ref) for cid, ref in refs if ref not in ids]
    assert not dangling, f"canvas references with no canonical record: {dangling}"
    # And there should actually be at least one canvas referencing something.
    assert refs, "expected the worked example to include at least one canvas with refs"
