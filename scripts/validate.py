#!/usr/bin/env python3
"""Validate Huginn Product Knowledge records against the JSON Schemas.

Usage:
    python scripts/validate.py [PATH ...]

Each PATH may be a file or a directory. Directories are searched recursively for
.yaml/.yml/.json records. Every record must carry a `kind` that maps to a schema
(see scripts/huginn_pk.py::KIND_TO_SCHEMA). Exit code is non-zero if anything fails.
"""
from __future__ import annotations

import pathlib
import sys

import huginn_pk as pk


def validate_path(path: pathlib.Path) -> tuple[int, int]:
    ok = bad = 0
    files = [path] if path.is_file() else list(pk.iter_record_files(path))
    for f in files:
        try:
            record = pk.load_record(f)
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"FAIL  {f}: could not parse ({exc})")
            bad += 1
            continue
        if not isinstance(record, dict) or "kind" not in record:
            # Skip non-record files (e.g. config yaml without a `kind`).
            continue
        errors = pk.validate_record(record)
        if errors:
            bad += 1
            print(f"FAIL  {f}  [{record.get('kind')}]")
            for e in errors:
                print(f"        - {e}")
        else:
            ok += 1
            print(f"ok    {f}  [{record.get('kind')}] {record.get('id', '')}")
    return ok, bad


def main(argv: list[str]) -> int:
    paths = [pathlib.Path(a) for a in argv] or [pk.TEMPLATE_DIR]
    total_ok = total_bad = 0
    for p in paths:
        if not p.exists():
            print(f"FAIL  {p}: no such path")
            total_bad += 1
            continue
        ok, bad = validate_path(p)
        total_ok += ok
        total_bad += bad
    print(f"\n{total_ok} valid, {total_bad} invalid")
    return 1 if total_bad else 0


if __name__ == "__main__":
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    raise SystemExit(main(sys.argv[1:]))
