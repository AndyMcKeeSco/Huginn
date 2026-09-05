#!/usr/bin/env python3
"""Scaffold a new canonical Product Knowledge record from a template.

Usage:
    python scripts/new_record.py <kind> [--title "..."] [--id PREFIX-slug] [--out DIR]

Example:
    python scripts/new_record.py opportunity --title "Users cannot find their case reference"

Prints the new record to stdout, or writes it to --out/<id>.yaml if --out is given.
The generated id is derived from the title (or a counter) so it is stable and human-readable;
review it before committing.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import huginn_pk as pk

ID_PREFIX = {
    "intent": "INT",
    "opportunity": "OPP",
    "proposition": "PROP",
    "test": "TEST",
    "evidence": "EV",
    "learning": "LRN",
    "solution": "SOL",
    "decision": "DEC",
    "sprint": "SPR",
    "sprint_outcome": "SPO",
    "pivot_persevere_review": "PPR",
    "pivot_reframe_recommendation": "PRR",
    "artifact_ref": "ART",
    "signal": "SIG",
    "canvas": "CNV",
    "decision_brief": "DB",
}

# kind -> template filename stem (mirrors templates/*.template.yaml)
TEMPLATE_STEM = {
    "sprint_outcome": "sprint-outcome",
    "pivot_persevere_review": "pivot-persevere-review",
    "pivot_reframe_recommendation": "pivot-reframe-recommendation",
    "artifact_ref": "artifact-ref",
    "decision_brief": "decision-brief",
}


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:48] or "new"


def template_path(kind: str) -> pathlib.Path:
    stem = TEMPLATE_STEM.get(kind, kind)
    return pk.TEMPLATE_DIR / f"{stem}.template.yaml"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=sorted(ID_PREFIX))
    parser.add_argument("--title", default="")
    parser.add_argument("--id", dest="record_id", default=None)
    parser.add_argument("--out", default=None, help="Directory to write <id>.yaml into.")
    args = parser.parse_args(argv)

    tpl = template_path(args.kind)
    if not tpl.exists():
        print(f"No template for kind {args.kind!r} at {tpl}", file=sys.stderr)
        return 2

    text = tpl.read_text(encoding="utf-8")
    record_id = args.record_id or f"{ID_PREFIX[args.kind]}-{slugify(args.title) if args.title else 'new'}"

    # Replace the placeholder id line and, where present, the statement/title line.
    text = re.sub(r"^id:.*$", f"id: {record_id}", text, count=1, flags=re.MULTILINE)
    if args.title:
        text = re.sub(
            r'^(statement|title):.*$',
            lambda m: f'{m.group(1)}: "{args.title}"',
            text,
            count=1,
            flags=re.MULTILINE,
        )

    if args.out:
        out_dir = pathlib.Path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{record_id}.yaml"
        out_path.write_text(text, encoding="utf-8")
        print(f"Wrote {out_path}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    raise SystemExit(main(sys.argv[1:]))
