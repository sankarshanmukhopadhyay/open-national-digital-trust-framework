#!/usr/bin/env python3
"""Inspect the generated Jekyll site for publication-breaking defects.

The check parses HTML structurally so that search-index text embedded by Just the
Docs does not create false positives. It verifies Mermaid integration, confirms
that every published Markdown source produced HTML, rejects rendered links that
still expose ``.md`` paths, and resolves internal links against the generated
site.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
import re
import sys
import yaml


MERMAID_RUNTIME_MARKERS = (
    "mermaid.esm.min.mjs",
    "mermaid.min.js",
    "cdn.jsdelivr.net/npm/mermaid",
)
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}


class PageInspector(HTMLParser):
    """Collect Mermaid blocks, runtime references, and real anchor targets."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.mermaid_blocks = 0
        self.runtime_present = False
        self.hrefs: list[str] = []
        self._ignored_depth = 0

    @staticmethod
    def _classes(attrs: list[tuple[str, str | None]]) -> set[str]:
        value = next((v for k, v in attrs if k == "class"), None) or ""
        return set(value.split())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)

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

        if tag == "a" and attrs_dict.get("href"):
            self.hrefs.append(attrs_dict["href"] or "")

        classes = self._classes(attrs)
        if ("language-mermaid" in classes or "mermaid" in classes) and tag in {"code", "pre", "div"}:
            self.mermaid_blocks += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._ignored_depth and any(marker in data for marker in MERMAID_RUNTIME_MARKERS):
            self.runtime_present = True


def inspect_page(path: Path) -> PageInspector:
    parser = PageInspector()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    parser.close()
    return parser


def load_baseurl() -> str:
    config = Path("_config.yml")
    if not config.exists():
        return ""
    payload = yaml.safe_load(config.read_text(encoding="utf-8")) or {}
    return str(payload.get("baseurl") or "").rstrip("/")


def source_output(source: Path, site: Path) -> Path:
    rel = source.as_posix()
    return site / (rel[:-3] + ".html")


def candidate_targets(site: Path, current: Path, href_path: str, baseurl: str) -> list[Path]:
    decoded = unquote(href_path)
    if baseurl and (decoded == baseurl or decoded.startswith(baseurl + "/")):
        decoded = decoded[len(baseurl):] or "/"

    if decoded.startswith("/"):
        relative = decoded.lstrip("/")
    else:
        relative = str(PurePosixPath(current.relative_to(site).parent.as_posix()) / decoded)

    # Collapse dot segments without allowing traversal outside _site.
    parts: list[str] = []
    for part in PurePosixPath(relative).parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    clean = Path(*parts) if parts else Path()
    target = site / clean

    candidates = [target]
    if decoded.endswith("/") or not clean.name:
        candidates.append(target / "index.html")
    elif not clean.suffix:
        candidates.extend([target.with_suffix(".html"), target / "index.html"])
    return candidates


def main() -> int:
    site = Path("_site")
    errors: list[str] = []
    baseurl = load_baseurl()

    if not site.exists():
        errors.append("_site does not exist")

    html = list(site.rglob("*.html")) if site.exists() else []
    if not html:
        errors.append("No generated HTML pages found")

    # Publication coverage: each source page intended for Pages must exist.
    sources = sorted(Path("docs").rglob("*.md")) + sorted(Path("profiles").rglob("*.md"))
    for source in sources:
        output = source_output(source, site)
        if not output.exists():
            errors.append(f"Published source has no generated page: {source} -> {output}")

    mermaid_pages = 0
    mermaid_blocks = 0
    checked_links = 0

    for path in html:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "```mermaid" in text:
            errors.append(f"Unprocessed Mermaid fence in {path}")
        if "Diagram could not be rendered." in text:
            errors.append(f"Legacy Mermaid fallback text present in {path}")

        inspector = inspect_page(path)
        if inspector.mermaid_blocks:
            mermaid_pages += 1
            mermaid_blocks += inspector.mermaid_blocks
            if not inspector.runtime_present:
                errors.append(f"Mermaid runtime missing from diagram page {path}")

        for href in inspector.hrefs:
            parsed = urlsplit(href)
            if parsed.scheme.lower() in IGNORED_SCHEMES or parsed.netloc or not parsed.path:
                continue
            checked_links += 1
            link_path = unquote(parsed.path)
            if re.search(r"\.(?:md|markdown)$", link_path, re.IGNORECASE):
                errors.append(f"Rendered Markdown link in {path}: {href}")
                continue
            if not any(candidate.exists() for candidate in candidate_targets(site, path, parsed.path, baseurl)):
                errors.append(f"Broken generated-site link in {path}: {href}")

    if errors:
        print("\n".join(errors))
        return 1

    print(
        "Built-site check passed: "
        f"{len(html)} HTML files inspected; "
        f"{len(sources)} published sources confirmed; "
        f"{checked_links} internal links resolved; "
        f"{mermaid_pages} pages contain {mermaid_blocks} Mermaid block(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
