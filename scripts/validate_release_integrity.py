#!/usr/bin/env python3
"""Validate release metadata, bindings, licences, and authoritative registers."""
from pathlib import Path
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def load_yaml(rel):
    try:
        return yaml.safe_load((ROOT / rel).read_text(encoding="utf-8")) or {}
    except Exception as exc:
        errors.append(f"{rel}: invalid YAML: {exc}")
        return {}


def normalise(value):
    return str(value).strip().lstrip("v")

# Current release metadata must resolve to the same version.
metadata_versions = {
    "PROJECT-STATUS.yaml": load_yaml("PROJECT-STATUS.yaml").get("version"),
    "CITATION.cff": load_yaml("CITATION.cff").get("version"),
    f"model/releases/v{version}.yaml": load_yaml(f"model/releases/v{version}.yaml").get("framework_version"),
}
for rel, declared in metadata_versions.items():
    if normalise(declared) != version:
        errors.append(f"{rel}: version '{declared}' does not match VERSION '{version}'")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if f"v{version}" not in readme:
    errors.append(f"README.md does not declare current release v{version}")

# Binding declarations are compatibility evidence and must match the current release.
for path in sorted((ROOT / "bindings").rglob("*.json")):
    rel = path.relative_to(ROOT)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{rel}: invalid JSON: {exc}")
        continue
    if normalise(payload.get("ondtfVersion")) != version:
        errors.append(f"{rel}: ondtfVersion '{payload.get('ondtfVersion')}' does not match VERSION '{version}'")
    review = payload.get("reviewStatus") or {}
    if review.get("status") != "current":
        errors.append(f"{rel}: reviewStatus.status must be 'current'")
    if normalise(review.get("reviewedAgainstOndtfVersion")) != version:
        errors.append(f"{rel}: reviewedAgainstOndtfVersion must match VERSION '{version}'")
    if not review.get("reviewedOn") or not review.get("reviewBasis") or not review.get("result"):
        errors.append(f"{rel}: current review evidence is incomplete")

# LICENSE is canonical; current metadata must use its SPDX-compatible identifier.
license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
if "Creative Commons Attribution 4.0 International" not in license_text:
    errors.append("LICENSE is not the expected Creative Commons Attribution 4.0 International text")
if "CC BY 4.0" not in readme:
    errors.append("README.md does not declare CC BY 4.0")
if load_yaml("CITATION.cff").get("license") != "CC-BY-4.0":
    errors.append("CITATION.cff license must be CC-BY-4.0")

# Authoritative machine-readable paths must never contain unresolved authoring scaffolding.
placeholder_patterns = [
    re.compile(r"\b(?:DEP|ADOPT)-EXAMPLE-\d+\b", re.I),
    re.compile(r"replace with", re.I),
    re.compile(r"<\s*(?:authoritative|selected|version|dependency|adopted|bounded)", re.I),
    re.compile(r"\bTODO\b|\bTBD\b", re.I),
]
authoritative_roots = [ROOT / "model", ROOT / "bindings", ROOT / "governance", ROOT / "data"]
for base in authoritative_roots:
    for path in base.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".yaml", ".yml", ".json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in placeholder_patterns:
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: unresolved placeholder matches /{pattern.pattern}/")
                break

# Active registers must state authority and keep entry_count synchronized.
for rel, key in [
    ("model/profiles/dependency-register.yaml", "dependencies"),
    ("model/profiles/external-adoption-register.yaml", "adoptions"),
]:
    payload = load_yaml(rel)
    register = payload.get("register") or {}
    entries = payload.get(key)
    if register.get("authoritative") is not True or register.get("status") != "active":
        errors.append(f"{rel}: register must be active and authoritative")
    if not isinstance(entries, list):
        errors.append(f"{rel}: {key} must be a list")
    elif register.get("entry_count") != len(entries):
        errors.append(f"{rel}: register.entry_count does not match {key} length")

if errors:
    print("Release integrity validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Release integrity validation passed: v{version} metadata, bindings, licences and authoritative registers are coherent.")
