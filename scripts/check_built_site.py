#!/usr/bin/env python3
"""Inspect the generated Jekyll site for publication-breaking defects.

The check deliberately parses HTML instead of searching the complete document as
plain text. Just the Docs embeds the searchable content of the whole site in a
JavaScript search index. A raw string search therefore reports Mermaid classes
on pages that contain no Mermaid diagram of their own.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys


MERMAID_RUNTIME_MARKERS = (
    "mermaid.esm.min.mjs",  # Mermaid 10+ used by current Just the Docs
    "mermaid.min.js",       # Mermaid 9 and earlier / local legacy path
    "cdn.jsdelivr.net/npm/mermaid",
)


class PageInspector(HTMLParser):
    """Collect rendered Mermaid blocks and runtime references from real markup."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.mermaid_blocks = 0
        self.runtime_present = False
        self._ignored_depth = 0

    @staticmethod
    def _classes(attrs: list[tuple[str, str | None]]) -> set[str]:
        value = next((v for k, v in attrs if k == "class"), None) or ""
        return set(value.split())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)

        # Runtime detection must include script tags, including ESM imports used
        # by Mermaid >= 10 and Just the Docs 0.12.
        if tag == "script":
            src = attrs_dict.get("src") or ""
            if any(marker in src for marker in MERMAID_RUNTIME_MARKERS):
                self.runtime_present = True
            self._ignored_depth += 1
            return

        if tag == "style":
            self._ignored_depth += 1
            return

        if self._ignored_depth:
            return

        classes = self._classes(attrs)
        if "language-mermaid" in classes or "mermaid" in classes:
            # Just the Docs/kramdown normally emits <code class="language-mermaid">.
            # The generic "mermaid" class also supports pre-render wrappers.
            if tag in {"code", "pre", "div"}:
                self.mermaid_blocks += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        # Just the Docs 0.12 injects an inline module script that imports Mermaid.
        if self._ignored_depth and any(marker in data for marker in MERMAID_RUNTIME_MARKERS):
            self.runtime_present = True


def inspect_page(path: Path) -> tuple[int, bool]:
    parser = PageInspector()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    parser.close()
    return parser.mermaid_blocks, parser.runtime_present


def main() -> int:
    site = Path("_site")
    errors: list[str] = []

    if not site.exists():
        errors.append("_site does not exist")

    html = list(site.rglob("*.html")) if site.exists() else []
    if not html:
        errors.append("No generated HTML pages found")

    mermaid_pages = 0
    mermaid_blocks = 0

    for path in html:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "```mermaid" in text:
            errors.append(f"Unprocessed Mermaid fence in {path}")
        if "Diagram could not be rendered." in text:
            errors.append(f"Legacy Mermaid fallback text present in {path}")

        blocks, runtime_present = inspect_page(path)
        if blocks:
            mermaid_pages += 1
            mermaid_blocks += blocks
            if not runtime_present:
                errors.append(f"Mermaid runtime missing from diagram page {path}")

    if errors:
        print("\n".join(errors))
        return 1

    print(
        "Built-site check passed: "
        f"{len(html)} HTML files inspected; "
        f"{mermaid_pages} pages contain {mermaid_blocks} Mermaid block(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
