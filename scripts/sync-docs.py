#!/usr/bin/env python3
"""Generate MkDocs pages from root-level canonical markdown sources."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SOURCE_DIRS = (
    "case-studies",
    "checklists",
    "examples",
    "frameworks",
    "templates",
)
CTA_INCLUDE = '--8<-- "_includes/cta.md"'


def strip_generated_cta(content: str) -> str:
    stripped = content.rstrip()
    if stripped.endswith(CTA_INCLUDE):
        stripped = stripped[: -len(CTA_INCLUDE)].rstrip()
    return stripped


def generated_content(source: Path) -> str:
    content = strip_generated_cta(source.read_text(encoding="utf-8"))
    return f"{content}\n\n{CTA_INCLUDE}\n"


def expected_pages() -> dict[Path, str]:
    pages: dict[Path, str] = {}
    for source_dir in SOURCE_DIRS:
        for source in sorted((ROOT / source_dir).glob("*.md")):
            pages[DOCS / source_dir / source.name] = generated_content(source)
    return pages


def sync_docs() -> None:
    pages = expected_pages()
    for source_dir in SOURCE_DIRS:
        target_dir = DOCS / source_dir
        if target_dir.exists():
            shutil.rmtree(target_dir)
        target_dir.mkdir(parents=True)

    for target, content in pages.items():
        target.write_text(content, encoding="utf-8")


def check_docs() -> int:
    pages = expected_pages()
    failures: list[str] = []

    for source_dir in SOURCE_DIRS:
        target_dir = DOCS / source_dir
        expected_targets = {path for path in pages if path.parent == target_dir}
        actual_targets = set(target_dir.glob("*.md")) if target_dir.exists() else set()

        for missing in sorted(expected_targets - actual_targets):
            failures.append(f"missing generated page: {missing.relative_to(ROOT)}")
        for extra in sorted(actual_targets - expected_targets):
            failures.append(f"unexpected generated page: {extra.relative_to(ROOT)}")

    for target, expected in sorted(pages.items()):
        if not target.exists():
            continue
        actual = target.read_text(encoding="utf-8")
        if actual != expected:
            failures.append(f"out-of-sync generated page: {target.relative_to(ROOT)}")

    if failures:
        print("Generated docs are not synced with root-level sources:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        print("Run `python scripts/sync-docs.py --write`.", file=sys.stderr)
        return 1

    return 0


def on_pre_build(config, **kwargs) -> None:  # noqa: ANN001
    sync_docs()


def on_files(files, config, **kwargs):  # noqa: ANN001, ANN201
    # MkDocs excludes /templates/ by default because it is often used for theme
    # overrides. Here it is a public content section, so opt it back in.
    from mkdocs.structure.files import InclusionLevel

    for file in files:
        if file.src_uri.startswith("templates/"):
            file.inclusion = InclusionLevel.INCLUDED
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify generated docs match canonical sources")
    parser.add_argument("--write", action="store_true", help="write generated docs to docs/")
    args = parser.parse_args()

    if args.check:
        return check_docs()

    sync_docs()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
