#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

root = Path(__file__).resolve().parents[1]
errors = []
path = root / 'model/project/maturation-register.yaml'
try:
    data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
except Exception as exc:
    print(f'Invalid maturation register: {exc}')
    sys.exit(1)

allowed_releases = {'v0.6.0', 'v0.7.0', 'v0.8.0', 'v0.9.0'}
allowed_destinations = {'core', 'profile', 'implementation_guidance'}
allowed_statuses = {'open', 'in_progress', 'evidence_available', 'closed'}

def unique(records, kind):
    ids = [r.get('id') for r in records]
    missing = [i for i, value in enumerate(ids) if not value]
    if missing:
        errors.append(f'{kind} records missing IDs at indexes: {missing}')
    dup = sorted({x for x in ids if x and ids.count(x) > 1})
    if dup:
        errors.append(f'Duplicate {kind} IDs: {dup}')
    return set(x for x in ids if x)

limitations = data.get('limitations') or []
issues = data.get('issues') or []
programmes = data.get('programmes') or []
patterns = data.get('patterns') or []
families = data.get('external_framework_families') or []
gates = data.get('release_gates') or []

lim_ids = unique(limitations, 'limitation')
issue_ids = unique(issues, 'issue')
programme_ids = unique(programmes, 'programme')
pattern_ids = unique(patterns, 'pattern')
family_ids = unique(families, 'framework-family')

for rec in limitations:
    if rec.get('type') not in {'enduring', 'reducible', 'maintained'}:
        errors.append(f"{rec.get('id')}: invalid limitation type")
    linked = rec.get('linked_issues') or []
    if rec.get('type') == 'reducible' and not linked:
        errors.append(f"{rec.get('id')}: reducible limitation requires linked issues")
    for ref in linked:
        if ref not in issue_ids:
            errors.append(f"{rec.get('id')}: unknown issue {ref}")

for rec in programmes:
    for release in rec.get('target_releases') or []:
        if release not in allowed_releases:
            errors.append(f"{rec.get('id')}: invalid target release {release}")
    for ref in rec.get('linked_issues') or []:
        if ref not in issue_ids:
            errors.append(f"{rec.get('id')}: unknown issue {ref}")

for rec in issues:
    rid = rec.get('id')
    for field in ('title', 'risk', 'target_release', 'owner_role', 'closure_evidence', 'status'):
        if not rec.get(field):
            errors.append(f'{rid}: missing required field {field}')
    if rec.get('target_release') not in allowed_releases:
        errors.append(f"{rid}: invalid target release {rec.get('target_release')}")
    if rec.get('status') not in allowed_statuses:
        errors.append(f"{rid}: invalid status {rec.get('status')}")
    if not rec.get('programmes'):
        errors.append(f'{rid}: at least one programme is required')
    for ref in rec.get('programmes') or []:
        if ref not in programme_ids:
            errors.append(f'{rid}: unknown programme {ref}')
    for ref in rec.get('patterns') or []:
        if ref not in pattern_ids:
            errors.append(f'{rid}: unknown pattern {ref}')

for rec in patterns:
    rid = rec.get('id')
    for field in ('title', 'destination', 'target_release', 'adoption_status', 'rationale', 'safeguards', 'evidence_required'):
        if not rec.get(field):
            errors.append(f'{rid}: missing required field {field}')
    if rec.get('destination') not in allowed_destinations:
        errors.append(f"{rid}: invalid destination {rec.get('destination')}")
    if rec.get('target_release') not in allowed_releases:
        errors.append(f"{rid}: invalid target release {rec.get('target_release')}")
    for ref in rec.get('source_families') or []:
        if ref not in family_ids:
            errors.append(f'{rid}: unknown source family {ref}')

for gate in gates:
    release = gate.get('release')
    if release not in allowed_releases:
        errors.append(f'Invalid release gate: {release}')
    for ref in gate.get('required_programmes') or []:
        if ref not in programme_ids:
            errors.append(f'{release}: unknown required programme {ref}')
    for ref in gate.get('required_issue_progress') or []:
        if ref not in issue_ids:
            errors.append(f'{release}: unknown required issue {ref}')

views = {
    'docs/project/known-limitations.md': lim_ids,
    'docs/project/unresolved-issues.md': issue_ids,
    'docs/project/future-work.md': programme_ids,
    'docs/project/external-framework-pattern-adoption.md': pattern_ids,
}
for rel, expected in views.items():
    text = (root / rel).read_text(encoding='utf-8')
    missing = sorted(x for x in expected if x not in text)
    if missing:
        errors.append(f'{rel} does not expose registered IDs: {missing}')

required_pages = [
    'external-framework-pattern-adoption.md', 'maturation-governance.md',
    'release-gates.md', 'implementation-evidence.md', 'adoption-roadmap.md'
]
index = (root / 'docs/project/index.md').read_text(encoding='utf-8')
site_map = (root / 'docs/site-map.md').read_text(encoding='utf-8')
for name in required_pages:
    if name not in index:
        errors.append(f'Project index does not link to {name}')
    if name[:-3] + '.html' not in site_map:
        errors.append(f'Site map does not link to {name[:-3]}.html')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'Maturation validation passed: {len(lim_ids)} limitations, {len(issue_ids)} issues, {len(programme_ids)} programmes, {len(pattern_ids)} adoption patterns and {len(gates)} release gates checked.')
