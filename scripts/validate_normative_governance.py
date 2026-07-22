#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import yaml

root = Path(__file__).resolve().parents[1]
errors = []

roles_path = root / 'model/governance/institutional-role-catalogue.yaml'
assign_path = root / 'model/governance/responsibility-assignment.yaml'
req_path = root / 'model/normative/requirement-catalogue.yaml'
schema_path = root / 'model/normative/requirement-schema.json'

try:
    roles_data = yaml.safe_load(roles_path.read_text(encoding='utf-8')) or {}
    assign_data = yaml.safe_load(assign_path.read_text(encoding='utf-8')) or {}
    req_data = yaml.safe_load(req_path.read_text(encoding='utf-8')) or {}
    json.loads(schema_path.read_text(encoding='utf-8'))
except Exception as exc:
    print(f'Normative/governance artefact parse failure: {exc}')
    sys.exit(1)

roles = roles_data.get('roles') or []
role_ids = [r.get('id') for r in roles]
role_set = {x for x in role_ids if x}
if len(role_set) != len(role_ids):
    errors.append('Institutional role IDs must be present and unique')
for role in roles:
    rid = role.get('id')
    for field in ('title', 'purpose', 'authority_source', 'minimum_evidence'):
        if not role.get(field): errors.append(f'{rid}: missing {field}')
    for ref_field in ('accountable_to',):
        ref = role.get(ref_field)
        if ref and ref.startswith('ROLE-') and ref not in role_set:
            errors.append(f'{rid}: unknown {ref_field} {ref}')
    for ref in role.get('appoints_or_recognises') or []:
        if ref not in role_set: errors.append(f'{rid}: unknown appointed role {ref}')

allowed_force = {'MUST','MUST_NOT','SHOULD','SHOULD_NOT','MAY'}
allowed_app = {'core','institutional','scheme','provider','service','implementation','interaction','affected-party','profile'}
reqs = req_data.get('requirements') or []
req_ids = [r.get('id') for r in reqs]
if len(set(req_ids)) != len(req_ids): errors.append('Requirement IDs must be unique')
pat = re.compile(r'^ONDTF-[A-Z]{3}-\d{3}$')
for req in reqs:
    rid=req.get('id')
    if not rid or not pat.match(rid): errors.append(f'Invalid requirement ID {rid}')
    for field in ('domain','force','statement','applicability','assessed_object','accountable_role','responsible_roles','evidence','status','introduced'):
        if not req.get(field): errors.append(f'{rid}: missing {field}')
    if req.get('force') not in allowed_force: errors.append(f'{rid}: invalid force')
    if not set(req.get('applicability') or []).issubset(allowed_app): errors.append(f'{rid}: invalid applicability')
    if req.get('accountable_role') not in role_set: errors.append(f"{rid}: unknown accountable role {req.get('accountable_role')}")
    for ref in req.get('responsible_roles') or []:
        if ref not in role_set: errors.append(f'{rid}: unknown responsible role {ref}')

for row in assign_data.get('assignments') or []:
    if not row.get('activity'): errors.append('Responsibility assignment missing activity')
    for field in ('accountable','responsible','consulted','informed'):
        value=row.get(field)
        refs=[value] if isinstance(value,str) else (value or [])
        for ref in refs:
            if ref not in role_set: errors.append(f"{row.get('activity')}: unknown {field} role {ref}")

required_docs = [
 'docs/normative/index.md','docs/normative/requirements-conventions.md','docs/normative/applicability-and-scoping.md',
 'docs/normative/profile-requirement-inheritance.md','docs/normative/exceptions-and-risk-acceptance.md','docs/normative/requirements-traceability.md',
 'docs/governance/institutional-operating-model.md','docs/governance/governing-authority.md','docs/governance/administrative-authority.md',
 'docs/governance/supervisory-and-regulatory-roles.md','docs/governance/accreditation-and-assessment-roles.md',
 'docs/governance/registry-and-trust-list-operators.md','docs/governance/appeals-redress-and-oversight.md','docs/governance/separation-of-duties.md']
for rel in required_docs:
    if not (root/rel).exists(): errors.append(f'Missing required page {rel}')

normative_text='\n'.join((root/p).read_text(encoding='utf-8') for p in required_docs if (root/p).exists())
for rid in ('ONDTF-GOV-001','ONDTF-ROL-001','ONDTF-ROL-007','ONDTF-CON-001'):
    if rid not in req_path.read_text(encoding='utf-8'): errors.append(f'Catalogue missing baseline requirement {rid}')
for role in ('ROLE-GA','ROLE-FA','ROLE-SA','ROLE-CAB','ROLE-CAR','ROLE-IO'):
    if role not in roles_path.read_text(encoding='utf-8'): errors.append(f'Role catalogue missing {role}')

if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'Normative/governance validation passed: {len(reqs)} requirements, {len(role_set)} roles and {len(assign_data.get("assignments") or [])} responsibility assignments checked.')
