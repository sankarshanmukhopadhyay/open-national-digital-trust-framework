#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
root=Path(__file__).resolve().parents[1]
errors=[]
for rel in ['model/assurance/risk-register-schema.yaml','model/assurance/conformance-assertion-schema.yaml','model/references/standards-register.yaml','model/references/nist-csf-2.0-crosswalk.yaml']:
    p=root/rel
    if not p.exists(): errors.append(f'Missing {rel}'); continue
    try: yaml.safe_load(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'Invalid YAML {rel}: {e}')
reg=yaml.safe_load((root/'model/references/standards-register.yaml').read_text(encoding='utf-8'))
ids=[]
for item in reg.get('references',[]):
    for field in ['id','publisher','title','status','class','canonical_url','last_reviewed']:
        if not item.get(field): errors.append(f"Reference {item.get('id','<unknown>')} missing {field}")
    ids.append(item.get('id'))
if len(ids)!=len(set(ids)): errors.append('Duplicate standards identifiers')
if errors:
    print('Assurance/reference validation failed:')
    print('\n'.join(f'- {e}' for e in errors)); sys.exit(1)
print(f'Assurance/reference validation passed: {len(ids)} standards registered.')
