#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

root = Path(__file__).resolve().parents[1]
errors = []


def load_yaml(path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        errors.append(f"Invalid YAML {path.relative_to(root)}: {exc}")
        return {}


maturity = load_yaml(root / "governance" / "maturity.yaml")
readiness = load_yaml(root / "governance" / "v1.0-readiness.yaml")

required = maturity.get("specification", {}).get("promotion", {}).get("v1.0.0", {}).get(
    "required_repository_controlled_gates", []
)
entries = readiness.get("gates", [])
ids = [entry.get("id") for entry in entries]

if len(ids) != len(set(ids)):
    errors.append("v1.0 readiness register contains duplicate gate IDs")

required_set = set(required)
registered_set = set(ids)
if registered_set != required_set:
    missing = sorted(required_set - registered_set)
    unknown = sorted(registered_set - required_set)
    if missing:
        errors.append("Missing required v1.0 gates: " + ", ".join(missing))
    if unknown:
        errors.append("Unknown v1.0 gates: " + ", ".join(unknown))

allowed_states = set(readiness.get("state_vocabulary", []))
expected_states = {"satisfied", "evidence-required", "blocked"}
if allowed_states != expected_states:
    errors.append("Readiness states must be exactly satisfied, evidence-required, blocked")

for entry in entries:
    gate_id = entry.get("id", "<missing-id>")
    state = entry.get("state")
    if state not in expected_states:
        errors.append(f"{gate_id}: invalid readiness state {state!r}")
    if entry.get("blocking") is not True:
        errors.append(f"{gate_id}: repository-controlled v1.0 gate must remain blocking")
    if not entry.get("judgment"):
        errors.append(f"{gate_id}: missing judgment")
    evidence = entry.get("evidence") or []
    if not evidence:
        errors.append(f"{gate_id}: missing evidence references")
    for ref in evidence:
        if isinstance(ref, str) and ref.startswith("https://"):
            continue
        if not (root / ref).exists():
            errors.append(f"{gate_id}: evidence reference does not exist: {ref}")
    residual = entry.get("residual_work")
    if state == "satisfied" and residual != "none":
        errors.append(f"{gate_id}: satisfied gate must declare residual_work: none")
    if state != "satisfied" and (not residual or residual == "none"):
        errors.append(f"{gate_id}: unsatisfied gate must declare concrete residual work")

promotion_ready = readiness.get("promotion_ready")
all_satisfied = bool(entries) and all(entry.get("state") == "satisfied" for entry in entries)
if promotion_ready is True and not all_satisfied:
    errors.append("promotion_ready cannot be true while any required gate is unsatisfied")
if promotion_ready is False and all_satisfied:
    errors.append("all gates are satisfied but promotion_ready remains false")

external = readiness.get("external_evidence", {})
if external.get("required_for_specification_promotion") is not False:
    errors.append("External evidence must not be required for specification promotion")
if external.get("current_level") != maturity.get("evidence", {}).get("current_level"):
    errors.append("Readiness external evidence level must match governance/maturity.yaml")

if errors:
    print("v1.0 readiness validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

satisfied = sum(1 for entry in entries if entry.get("state") == "satisfied")
print(
    f"v1.0 readiness validation passed: {satisfied}/{len(entries)} gates satisfied; "
    f"promotion_ready={str(promotion_ready).lower()}"
)
