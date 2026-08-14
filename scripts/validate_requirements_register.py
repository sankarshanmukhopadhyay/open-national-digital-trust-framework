#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
reqs=(yaml.safe_load((ROOT/'model/normative/requirement-catalogue.yaml').read_text()) or {}).get('requirements') or []
assertions_data=yaml.safe_load((ROOT/'conformance/candidate-assertions.yaml').read_text()) or {}
assertions=assertions_data.get('assertions') or assertions_data.get('candidate_assertions') or []
covered={x.get('requirement') for x in assertions if x.get('requirement')}
page=(ROOT/'docs/core-specification/requirements-register.md').read_text()
errors=[]
ids=[]
for req in reqs:
    rid=req.get('id'); ids.append(rid)
    if f'<a id="{rid.lower()}"></a>' not in page: errors.append(f'{rid}: missing stable register anchor')
    if f'### {rid}' not in page: errors.append(f'{rid}: missing register heading')
    if rid not in covered: errors.append(f'{rid}: no candidate conformance assertion')
    for field in ('statement','force','applicability','assessed_object','accountable_role','responsible_roles','evidence'):
        if not req.get(field): errors.append(f'{rid}: canonical catalogue missing {field}')
if len(ids)!=len(set(ids)): errors.append('duplicate requirement identifiers')
js=(ROOT/'assets/js/identifier-links.js').read_text()
if 'requirements-register.html#' not in js: errors.append('ONDTF identifier links do not route to Requirements Register')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'Requirements Register validation: PASS ({len(reqs)} requirements, {len(covered)} candidate mappings, stable direct links enabled)')
