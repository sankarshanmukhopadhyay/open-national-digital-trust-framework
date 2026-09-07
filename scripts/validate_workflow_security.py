#!/usr/bin/env python3
"""Fail closed on floating external GitHub Action refs and privileged trigger drift."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
SHA = re.compile(r"^[0-9a-f]{40}$")
USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")

errors = []
checked = 0

for path in sorted(list(WORKFLOWS.glob("*.yml")) + list(WORKFLOWS.glob("*.yaml"))):
    text = path.read_text(encoding="utf-8")
    if "permissions:" not in text:
        errors.append(f"{path.relative_to(ROOT)}: workflow must declare explicit permissions")
    if re.search(r"^\s*(pull_request_target|workflow_run)\s*:", text, re.MULTILINE):
        errors.append(
            f"{path.relative_to(ROOT)}: privileged trigger requires an explicit trust-boundary design before admission"
        )
    for lineno, line in enumerate(text.splitlines(), start=1):
        match = USES.match(line)
        if not match:
            continue
        value = match.group(1)
        if value.startswith("./"):
            continue
        checked += 1
        if "@" not in value:
            errors.append(f"{path.relative_to(ROOT)}:{lineno}: external action has no immutable ref: {value}")
            continue
        action, ref = value.rsplit("@", 1)
        if not SHA.fullmatch(ref):
            errors.append(
                f"{path.relative_to(ROOT)}:{lineno}: {action} must be pinned to a 40-character commit SHA, got {ref}"
            )

if checked == 0:
    errors.append("no external workflow actions found; security validation cannot establish pinning coverage")

if errors:
    print("workflow security validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"workflow security validation: PASS ({checked} external action references immutably pinned)")
