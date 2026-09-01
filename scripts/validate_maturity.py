#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

root = Path(__file__).resolve().parents[1]
path = root / "governance" / "maturity.yaml"
errors = []

try:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
except Exception as exc:
    print(f"Invalid governance/maturity.yaml: {exc}")
    sys.exit(1)

spec = data.get("specification", {})
evidence = data.get("evidence", {})

allowed = set(spec.get("allowed_maturity_states", []))
if allowed != {"draft", "candidate", "stable"}:
    errors.append("Specification maturity states must be exactly draft, candidate, stable")
if spec.get("maturity") not in allowed:
    errors.append("Current specification maturity is not an allowed state")

scale = evidence.get("scale", {})
expected_levels = {"E0", "E1", "E2", "E3", "E4"}
if set(scale) != expected_levels:
    errors.append("Evidence scale must define exactly E0 through E4")
if evidence.get("current_level") not in expected_levels:
    errors.append("Current evidence level must be one of E0 through E4")

promotion = spec.get("promotion", {}).get("v1.0.0", {})
if promotion.get("independent_implementation_required") is not False:
    errors.append("v1.0.0 specification promotion must not depend on independent implementation")
if promotion.get("external_evidence_state_must_be_declared") is not True:
    errors.append("v1.0.0 must require explicit external evidence-state declaration")

required_gates = set(promotion.get("required_repository_controlled_gates", []))
minimum_gates = {
    "normative-stability",
    "identifier-stability",
    "requirement-conformance-traceability",
    "deterministic-validation",
    "adversarial-negative-evidence",
    "compatibility-change-control",
    "errata-process",
    "blocking-issue-disposition",
    "release-integrity",
}
missing_gates = minimum_gates - required_gates
if missing_gates:
    errors.append("v1.0.0 promotion missing repository-controlled gates: " + ", ".join(sorted(missing_gates)))

independent = evidence.get("independent_implementation", {})
if "E2" not in independent.get("required_for", []):
    errors.append("Independent implementation must remain required for E2")
if independent.get("blocks_specification_promotion") is not False:
    errors.append("Independent implementation must not block specification promotion")

for key in ("cross_implementation_interoperability", "operational_deployment"):
    item = evidence.get(key, {})
    if item.get("blocks_specification_promotion") is not False:
        errors.append(f"{key} must not block specification promotion")

invalidation = evidence.get("invalidation", {})
if not invalidation.get("triggers"):
    errors.append("Evidence invalidation triggers must be declared")
if not invalidation.get("rule"):
    errors.append("Evidence invalidation rule must be declared")

if not data.get("governance_invariant"):
    errors.append("Governance invariant must be declared")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("ONDTF maturity and evidence governance validation passed.")
