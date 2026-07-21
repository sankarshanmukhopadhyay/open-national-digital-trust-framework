#!/usr/bin/env python3
"""Fail fast on Mermaid source patterns known to break browser rendering."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL)
ALLOWED = ("flowchart ", "graph ", "sequenceDiagram", "stateDiagram-v2", "classDiagram", "gantt")
LEGACY_DOTTED_LABEL = re.compile(r"-\.[A-Za-z]")
errors = []
count = 0
for path in sorted(list((ROOT / "docs").rglob("*.md")) + list((ROOT / "profiles").rglob("*.md")) + [ROOT / "README.md"]):
    text = path.read_text(encoding="utf-8")
    for index, match in enumerate(FENCE.finditer(text), start=1):
        count += 1
        source = match.group(1).strip()
        first = source.splitlines()[0].strip() if source else ""
        if not source:
            errors.append(f"{path}: diagram {index} is empty")
        elif not first.startswith(ALLOWED):
            errors.append(f"{path}: diagram {index} has unsupported declaration: {first}")
        if LEGACY_DOTTED_LABEL.search(source):
            errors.append(f"{path}: diagram {index} uses invalid dotted-edge label syntax")
        if "\\n" in source:
            errors.append(f"{path}: diagram {index} uses escaped newline in a label; use plain text")

if errors:
    print("Mermaid source validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"Mermaid source validation passed: {count} diagrams checked.")
