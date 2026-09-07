#!/usr/bin/env python3
from copy import deepcopy
from pathlib import Path
import hashlib
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

FREEZE_PATH = ROOT / "governance" / "v1.0-normative-freeze.yaml"
CHANGE_PATH = ROOT / "governance" / "v1.x-change-control.yaml"
ERRATA_PATH = ROOT / "governance" / "errata-and-emergency-change.yaml"
COVERAGE_PATH = ROOT / "governance" / "v1.0-adversarial-coverage.yaml"
REQ_PATH = ROOT / "model" / "normative" / "requirement-catalogue.yaml"
MANIFEST_PATH = ROOT / "model" / "project" / "normative-document-manifest.yaml"


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def git_blob_sha(path):
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def validate_freeze(obj):
    errors = []
    if obj.get("target_release") != "v1.0.0":
        errors.append("freeze target_release must be v1.0.0")
    if obj.get("state") != "release-decision-candidate":
        errors.append("freeze state must remain release-decision-candidate before release")
    surface = obj.get("normative_surface") or []
    ids = [x.get("id") for x in surface]
    expected_ids = {"NCP-001", "NCP-002", "NCP-003", "NCP-004", "NCP-005"}
    if set(ids) != expected_ids or len(ids) != len(expected_ids):
        errors.append("v1 normative surface must contain NCP-001 through NCP-005 exactly once")
    manifest = load(MANIFEST_PATH)
    manifest_by_id = {x.get("id"): x for x in manifest.get("artefacts", [])}
    for entry in surface:
        eid = entry.get("id", "<missing>")
        path_value = entry.get("path")
        if not path_value:
            errors.append(f"{eid}: missing path")
            continue
        path = ROOT / path_value
        if not path.exists() or not path.is_file():
            errors.append(f"{eid}: frozen artifact does not exist: {path_value}")
            continue
        manifest_entry = manifest_by_id.get(eid)
        if not manifest_entry or manifest_entry.get("path") != path_value:
            errors.append(f"{eid}: freeze path does not match normative document manifest")
        expected_sha = entry.get("git_blob_sha")
        actual_sha = git_blob_sha(path)
        if expected_sha != actual_sha:
            errors.append(f"{eid}: normative blob drift: expected {expected_sha}, got {actual_sha}")
    material = obj.get("material_normative_change") or {}
    required = set(material.get("requires") or [])
    required_controls = {
        "explicit change classification",
        "change-impact analysis",
        "migration determination",
        "evidence invalidation assessment",
        "reassessment of every affected v1 readiness gate",
        "governed release decision",
    }
    if not required_controls.issubset(required):
        errors.append("material normative change contract is missing required controls")
    if not obj.get("reassessment_triggers"):
        errors.append("freeze requires reassessment triggers")
    if (obj.get("decision_authority") or {}).get("bypass_allowed") is not False:
        errors.append("stable freeze bypass must be prohibited")
    return errors


def validate_change_control(obj):
    errors = []
    if obj.get("classification_required") is not True or obj.get("unknown_class_policy") != "reject":
        errors.append("change classification must be required and unknown classes rejected")
    classes = obj.get("change_classes") or {}
    if set(classes) != {"compatible", "materially-normative", "breaking"}:
        errors.append("change classes must be exactly compatible, materially-normative, breaking")
        return errors
    material = classes["materially-normative"]
    for field in (
        "migration_assessment_required",
        "evidence_invalidation_assessment_required",
        "assurance_reassessment_required",
        "change_impact_record_required",
    ):
        if material.get(field) is not True:
            errors.append(f"materially-normative: {field} must be true")
    breaking = classes["breaking"]
    for field in (
        "migration_required",
        "compatibility_evidence_required",
        "rollback_or_recovery_required",
        "evidence_invalidation_assessment_required",
        "assurance_reassessment_required",
        "affected_consumers_required",
        "change_impact_record_required",
    ):
        if breaking.get(field) is not True:
            errors.append(f"breaking: {field} must be true")
    if breaking.get("version_effect") != "major" or breaking.get("title_marker_required") != "!":
        errors.append("breaking changes must require major version and ! title marker")
    authority = obj.get("decision_authority") or {}
    if authority.get("breaking_exception_within_v1") != "prohibited":
        errors.append("breaking exceptions within v1 must be prohibited")
    return errors


def validate_errata(obj):
    errors = []
    expected_states = {
        "reported", "triaged", "accepted", "rejected", "ordinary-erratum",
        "emergency-correction", "published", "superseded", "reassessment-complete",
    }
    states = obj.get("states") or []
    if set(states) != expected_states or len(states) != len(expected_states):
        errors.append("errata lifecycle state vocabulary is incomplete or duplicated")
    transitions = obj.get("transitions") or []
    required_edges = {
        ("reported", "triaged"),
        ("triaged", "accepted"),
        ("triaged", "rejected"),
        ("accepted", "ordinary-erratum"),
        ("accepted", "emergency-correction"),
        ("ordinary-erratum", "published"),
        ("emergency-correction", "published"),
        ("published", "superseded"),
        ("superseded", "reassessment-complete"),
    }
    edges = {(x.get("from"), x.get("to")) for x in transitions}
    if not required_edges.issubset(edges):
        errors.append("errata lifecycle is missing a required transition")
    for index, transition in enumerate(transitions, start=1):
        if not transition.get("authority") or not transition.get("evidence"):
            errors.append(f"errata transition {index} lacks authority or evidence")
    emergency = obj.get("emergency_correction") or {}
    if not emergency.get("authority") or not emergency.get("maximum_scope"):
        errors.append("emergency correction must declare authority and maximum scope")
    required_fields = set(emergency.get("required_fields") or [])
    for field in ("expiry_or_review_at", "rollback_or_supersession_path", "evidence_invalidation_scope"):
        if field not in required_fields:
            errors.append(f"emergency correction must require {field}")
    must_trigger = set(emergency.get("must_trigger") or [])
    for control in ("evidence_invalidation_assessment", "affected_gate_reassessment", "independent_post_action_review"):
        if control not in must_trigger:
            errors.append(f"emergency correction must trigger {control}")
    return errors


def validate_coverage(obj):
    errors = []
    required_domains = set(obj.get("required_domains") or [])
    entries = obj.get("coverage") or []
    domains = [x.get("domain") for x in entries]
    if set(domains) != required_domains or len(domains) != len(required_domains):
        errors.append("adversarial coverage must contain every required domain exactly once")
    requirement_ids = {x.get("id") for x in load(REQ_PATH).get("requirements", [])}
    for entry in entries:
        domain = entry.get("domain", "<missing>")
        mode = entry.get("mode")
        if mode not in {"executable", "assessor"}:
            errors.append(f"{domain}: mode must be executable or assessor")
        refs = entry.get("requirements") or []
        if not refs:
            errors.append(f"{domain}: missing requirement references")
        unknown = set(refs) - requirement_ids
        if unknown:
            errors.append(f"{domain}: unknown requirement references: {', '.join(sorted(unknown))}")
        evidence = entry.get("evidence") or []
        if not evidence:
            errors.append(f"{domain}: missing evidence")
        for ref in evidence:
            if not (ROOT / ref).exists():
                errors.append(f"{domain}: evidence path does not exist: {ref}")
        if mode == "executable" and not entry.get("claim"):
            errors.append(f"{domain}: executable coverage requires a bounded claim")
        if mode == "assessor" and not entry.get("procedure"):
            errors.append(f"{domain}: assessor coverage requires an explicit procedure")
    if not obj.get("limitations"):
        errors.append("adversarial coverage must state limitations")
    return errors


freeze = load(FREEZE_PATH)
change = load(CHANGE_PATH)
errata = load(ERRATA_PATH)
coverage = load(COVERAGE_PATH)

errors = []
errors.extend(validate_freeze(freeze))
errors.extend(validate_change_control(change))
errors.extend(validate_errata(errata))
errors.extend(validate_coverage(coverage))

# Candidate normative metadata must not contradict the v0.9 candidate manifest.
roles = load(ROOT / "model" / "governance" / "institutional-role-catalogue.yaml")
lifecycle = load(ROOT / "model" / "operations" / "provider-lifecycle.yaml")
if roles.get("version") != "0.9.0-candidate" or roles.get("status") != "active":
    errors.append("institutional role catalogue metadata is not aligned to v0.9 candidate")
if lifecycle.get("version") != "0.9.0-candidate" or lifecycle.get("status") != "active":
    errors.append("provider lifecycle metadata is not aligned to v0.9 candidate")

# Deliberate falsification checks prove the validators reject the principal failure classes.
negative_failures = []
bad_freeze = deepcopy(freeze)
bad_freeze["normative_surface"][0]["git_blob_sha"] = "0" * 40
if not validate_freeze(bad_freeze):
    negative_failures.append("normative drift fixture was accepted")

bad_change = deepcopy(change)
bad_change["change_classes"]["breaking"]["migration_required"] = False
if not validate_change_control(bad_change):
    negative_failures.append("breaking-without-migration fixture was accepted")

bad_errata = deepcopy(errata)
bad_errata["emergency_correction"]["authority"] = ""
if not validate_errata(bad_errata):
    negative_failures.append("authority-free emergency correction fixture was accepted")

bad_coverage = deepcopy(coverage)
bad_coverage["coverage"] = bad_coverage["coverage"][:-1]
if not validate_coverage(bad_coverage):
    negative_failures.append("orphan adversarial-domain fixture was accepted")

errors.extend(negative_failures)

if errors:
    print("v1 stable controls validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    "v1 stable controls validation: PASS "
    f"({len(freeze['normative_surface'])} frozen normative artifacts, "
    f"{len(change['change_classes'])} change classes, "
    f"{len(errata['states'])} errata states, "
    f"{len(coverage['coverage'])} adversarial domains, 4 falsification fixtures)"
)
