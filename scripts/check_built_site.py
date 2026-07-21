#!/usr/bin/env python3
"""Validate the generated GitHub Pages site, including Mermaid integration."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SITE = Path("_site")
SOURCE_ROOTS = (Path("docs"), Path("profiles"))
MERMAID_FENCE = re.compile(r"^```mermaid\s*$", re.MULTILINE)
MERMAID_CODE = re.compile(
    r'<code\b[^>]*class=["\'][^"\']*\blanguage-mermaid\b[^"\']*["\']',
    re.IGNORECASE,
)


def source_diagram_count() -> int:
    total = 0
    for root in SOURCE_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            total += len(MERMAID_FENCE.findall(path.read_text(encoding="utf-8")))
    return total


def main() -> int:
    errors: list[str] = []

    if not SITE.exists():
        errors.append("_site does not exist")
        html_files: list[Path] = []
    else:
        html_files = list(SITE.rglob("*.html"))

    if not html_files:
        errors.append("No generated HTML pages found")

    generated_diagrams = 0
    mermaid_runtime_pages = 0

    for path in html_files:
        text = path.read_text(encoding="utf-8", errors="ignore")

        if "```mermaid" in text:
            errors.append(f"Unprocessed Mermaid fence in {path}")

        generated_diagrams += len(MERMAID_CODE.findall(text))

        # Just the Docs emits the Mermaid import and initialization component on
        # every page when site.mermaid is configured.
        has_mermaid_import = (
            "mermaid.esm.min.mjs" in text
            or "mermaid.min.js" in text
            or "cdn.jsdelivr.net/npm/mermaid@" in text
        )
        has_mermaid_initialization = (
            "mermaid.initialize" in text or "mermaid.run" in text
        )
        if has_mermaid_import and has_mermaid_initialization:
            mermaid_runtime_pages += 1

    expected_diagrams = source_diagram_count()
    if generated_diagrams != expected_diagrams:
        errors.append(
            "Generated Mermaid block count does not match source: "
            f"expected {expected_diagrams}, found {generated_diagrams}"
        )

    if html_files and mermaid_runtime_pages != len(html_files):
        errors.append(
            "Just the Docs Mermaid runtime was not present on every generated "
            f"page: {mermaid_runtime_pages}/{len(html_files)}"
        )

    if errors:
        print("\n".join(errors))
        return 1

    print(
        "Built-site check passed: "
        f"{len(html_files)} HTML files and {generated_diagrams} Mermaid diagrams inspected."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
