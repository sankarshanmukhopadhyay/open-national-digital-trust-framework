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

tech_q = next((q for q in question_model.get("questions", []) if q.get("id") == "GFC-TEC-001"), None)
expected_sequence = [
    "define-required-capabilities",
    "state-required-outcomes",
    "select-implementation-mechanisms",
    "record-substitutability-or-justified-exclusivity",
]
if not tech_q:
    errors.append("GFC-TEC-001 must exist")
else:
    if tech_q.get("selection_sequence") != expected_sequence:
        errors.append("GFC-TEC-001 must enforce capability-before-mechanism selection")
    if not {"capabilities", "dependencies"}.issubset(set(tech_q.get("maps_to", []))):
        errors.append("GFC-TEC-001 must map to both capabilities and dependencies")

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
    "model/profiles/external-adoption-taxonomy.yaml",
    "model/profiles/change-classification.yaml",
    "model/project/controlled-document-register.yaml",
]:
    load(rel)

taxonomy = load("model/profiles/external-adoption-taxonomy.yaml")
relationships = taxonomy.get("implementation_relationships", [])
relationship_ids = {x.get("id") for x in relationships}
expected_relationships = {"substitutable", "complementary", "required-companion", "profile-exclusive", "incompatible"}
if relationship_ids != expected_relationships:
    errors.append(f"External adoption taxonomy must define exactly {sorted(expected_relationships)}")
exclusive_types = {x.get("id") for x in relationships if x.get("exclusivity_requires_justification")}
if exclusive_types != {"required-companion", "profile-exclusive", "incompatible"}:
    errors.append("External adoption taxonomy has incorrect exclusivity-justification semantics")

adoption_template = load("templates/profiles/external-adoption-register-entry.template.yaml")
for field in ("capability", "required_outcomes", "ondtf_mapping", "implementation_relationship", "selection_constraints"):
    if field not in adoption_template:
        errors.append(f"External adoption template missing {field}")
rel = adoption_template.get("implementation_relationship", {})
if rel.get("type") not in relationship_ids:
    errors.append("External adoption template uses unknown implementation relationship")

live = load("model/profiles/external-adoption-register.yaml")
for item in live.get("adoptions", []):
    ident = item.get("id", "<unknown adoption>")
    for field in ("capability", "required_outcomes", "ondtf_mapping", "implementation_relationship"):
        if field not in item:
            errors.append(f"{ident}: missing {field}")
    relationship = item.get("implementation_relationship", {})
    kind = relationship.get("type")
    if kind not in relationship_ids:
        errors.append(f"{ident}: unknown implementation relationship {kind}")
    if kind in exclusive_types and not relationship.get("exclusivity_justification"):
        errors.append(f"{ident}: {kind} requires exclusivity_justification")
    if kind == "substitutable" and relationship.get("alternatives_permitted") is not True:
        errors.append(f"{ident}: substitutable adoption must permit alternatives")

maturation = load("model/project/maturation-register.yaml")
epa_ids = {x.get("id") for x in maturation.get("patterns", [])}
illustrations = load("examples/external-pattern-mappings/mapping-examples.yaml")
if illustrations.get("illustrative") is not True or illustrations.get("normative_effect") != "none":
    errors.append("External pattern examples must be explicitly illustrative and non-normative")
if len(illustrations.get("examples", [])) < 3:
    errors.append("Portability pressure test must include at least three materially different ecosystem examples")
for ex in illustrations.get("examples", []):
    for mapping in ex.get("mappings", []):
        if mapping.get("relationship") not in relationship_ids:
            errors.append(f"{ex.get('ecosystem')}: unknown relationship {mapping.get('relationship')}")
        if mapping.get("ondtf_pattern") not in epa_ids:
            errors.append(f"{ex.get('ecosystem')}: unknown ONDTF external-adoption pattern {mapping.get('ondtf_pattern')}")
        if not mapping.get("required_outcomes"):
            errors.append(f"{ex.get('ecosystem')}: mapping must declare required outcomes")

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
    "docs/adoption/portability-and-external-patterns.md",
    "docs/learning/framework-construction.md",
    "examples/worked-profile/index.md",
    "examples/worked-profile/validation-report.md",
    "examples/external-pattern-mappings/index.md",
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
    f"{len(question_ids)} questions, {len(patterns)} patterns, "
    f"{len(relationship_ids)} implementation relationships and "
    f"{len(rules)} contradiction rules checked; "
    f"{len(illustrations.get('examples', []))} portability examples remain informative."
)
