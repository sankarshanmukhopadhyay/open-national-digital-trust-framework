#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import yaml

root = Path(__file__).resolve().parents[1]
errors = []


def load(rel):
    p = root / rel
    if not p.exists():
        errors.append(f"Missing {rel}")
        return {}
    try:
        if p.suffix == ".json":
            return json.loads(p.read_text())
        return yaml.safe_load(p.read_text()) or {}
    except Exception as exc:
        errors.append(f"{rel}: parse failure: {exc}")
        return {}


profile_types_model = load("model/profiles/profile-types.yaml")
profile_types = [x.get("id") for x in profile_types_model.get("profile_types", [])]
if len(profile_types) != 5 or len(profile_types) != len(set(profile_types)):
    errors.append("Profile types must contain five unique entries")

for rel in [
    "model/profiles/profile-manifest.schema.json",
    "model/adoption/construction-response.schema.json",
]:
    load(rel)

question_model = load("model/adoption/question-catalogue.yaml")
question_ids = [x.get("id") for x in question_model.get("questions", [])]
if len(question_model.get("stages", [])) != 11:
    errors.append("Question catalogue must define eleven stages")
if len(question_ids) != len(set(question_ids)):
    errors.append("Question identifiers must be unique")
for item in question_model.get("questions", []):
    for field in ("id", "stage", "prompt", "response_type", "required", "maps_to", "review"):
        if field not in item:
            errors.append(f"{item.get('id')}: missing {field}")

patterns = load("model/adoption/pattern-catalogue.yaml").get("patterns", [])
pattern_ids = {x.get("id") for x in patterns}
for item in question_model.get("questions", []):
    for pattern_id in item.get("options", []):
        if pattern_id not in pattern_ids:
            errors.append(f"{item.get('id')}: unknown pattern {pattern_id}")

rules = load("model/adoption/contradiction-rules.yaml").get("rules", [])
for item in rules:
    for field in ("id", "severity", "when", "message", "review"):
        if not item.get(field):
            errors.append(f"Contradiction rule {item.get('id')}: missing {field}")

gates = load("model/adoption/completeness-gates.yaml")
for gate in gates.get("stage_gates", []):
    for question_id in gate.get("required_questions", []):
        if question_id not in question_ids:
            errors.append(f"Stage {gate.get('stage')}: unknown question {question_id}")

for rel in [
    "model/profiles/dependency-register.yaml",
    "model/profiles/external-adoption-register.yaml",
    "model/profiles/change-classification.yaml",
    "model/project/controlled-document-register.yaml",
]:
    load(rel)

required_docs = [
    "profiles/index.md",
    "profiles/profile-types.md",
    "profiles/profile-methodology.md",
    "profiles/profile-template.md",
    "profiles/profile-composition.md",
    "profiles/dependency-and-adoption-governance.md",
    "profiles/profile-versioning-and-change.md",
    "profiles/profile-validation.md",
    "docs/adoption/guided-framework-construction.md",
    "docs/adoption/construction-stages.md",
    "docs/adoption/decision-states-and-review-gates.md",
    "docs/adoption/contradiction-and-completeness.md",
    "docs/adoption/generated-artefacts.md",
    "docs/adoption/workshop-guide.md",
    "docs/adoption/guided-construction-model.md",
    "docs/learning/framework-construction.md",
    "examples/worked-profile/index.md",
    "examples/worked-profile/validation-report.md",
]
for rel in required_docs:
    if not (root / rel).exists():
        errors.append(f"Missing required page {rel}")

internal_label = re.compile(r"\bcommit\s+[0-9]+\b", re.IGNORECASE)
for base in [root / "docs", root / "profiles", root / "model", root / "templates"]:
    for path in base.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml", ".json"}:
            if internal_label.search(path.read_text(errors="ignore")):
                errors.append(f"Internal-only commit label found in {path.relative_to(root)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(
    "Profile/adoption validation passed: "
    f"{len(profile_types)} profile types, "
    f"{len(question_model.get('stages', []))} construction stages, "
    f"{len(question_ids)} questions, {len(patterns)} patterns and "
    f"{len(rules)} contradiction rules checked."
)
