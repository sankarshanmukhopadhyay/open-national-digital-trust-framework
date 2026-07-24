#!/usr/bin/env python3
import json
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []

def load_yaml(path):
    with path.open(encoding='utf-8') as f:
        return yaml.safe_load(f)

register = load_yaml(ROOT / 'model/references/standards-register.yaml')
sectors = load_yaml(ROOT / 'model/references/sector-taxonomy.yaml')
adoption = load_yaml(ROOT / 'model/references/adoption-taxonomy.yaml')
json.loads((ROOT / 'model/references/sector-standard-mapping.schema.json').read_text())

standard_ids = {r['id'] for r in register['references']}
sector_ids = {s['id'] for s in sectors['sectors']}
states = {s['id'] for s in adoption['adoption_states']}
modes = {m['id'] for m in adoption['adoption_modes']}

for path in sorted((ROOT / 'model/references/sector-standard-mappings').glob('*.yaml')):
    doc = load_yaml(path)
    if doc.get('sector_id') not in sector_ids:
        errors.append(f'{path}: unknown sector_id {doc.get("sector_id")}')
    if doc.get('status') != 'illustrative' and doc.get('authority', '').startswith('UNASSIGNED'):
        errors.append(f'{path}: non-illustrative mapping requires assigned authority')
    for item in doc.get('standards', []):
        if item.get('standard_id') not in standard_ids:
            errors.append(f'{path}: unknown standard_id {item.get("standard_id")}')
        if item.get('disposition') not in states:
            errors.append(f'{path}: invalid disposition {item.get("disposition")}')
        if item.get('adoption_mode') not in modes:
            errors.append(f'{path}: invalid adoption_mode {item.get("adoption_mode")}')
        if item.get('disposition') in {'candidate', 'adopted'}:
            for field in ('selected_scope', 'evidence_required', 'review'):
                if not item.get(field):
                    errors.append(f'{path}: {item.get("standard_id")} missing {field}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'Validated {len(sector_ids)} sectors and sector-standard mappings against {len(standard_ids)} registered references.')
