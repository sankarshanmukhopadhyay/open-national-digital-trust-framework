#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
root=Path(__file__).resolve().parents[1]
errors=[]
version=(root/'VERSION').read_text().strip()
if version!='0.6.0': errors.append(f'VERSION is {version}, expected 0.6.0')
required=['PROJECT-STATUS.yaml','CITATION.cff','model/releases/v0.6.0.yaml','release/RELEASE-NOTES-v0.6.0.md','release/MANIFEST-v0.6.0.md','release/CHECKLIST-v0.6.0.md','release/DOCUMENT-INVENTORY-v0.6.0.md','docs/project/v0.6-readiness-checklist.md']
for f in required:
    if not (root/f).exists(): errors.append(f'Missing {f}')
for f in ['PROJECT-STATUS.yaml','CITATION.cff','model/releases/v0.6.0.yaml']:
    try: yaml.safe_load((root/f).read_text())
    except Exception as e: errors.append(f'Invalid YAML {f}: {e}')
readme=(root/'README.md').read_text()
if 'v0.6.0' not in readme or 'Operational Framework Draft' not in readme: errors.append('README release status not updated')
reg=yaml.safe_load((root/'model/project/maturation-register.yaml').read_text())
closed={i['id'] for i in reg['issues'] if i.get('status')=='closed'}
expected={'URI-07','URI-08','URI-09','URI-10','URI-11','URI-12','URI-18','URI-19'}
if not expected.issubset(closed): errors.append(f'Expected v0.6.0 issue closures missing: {sorted(expected-closed)}')
if errors:
    print('Release validation failed:')
    for e in errors: print(f'- {e}')
    sys.exit(1)
print('Release validation passed: v0.6.0 Operational Framework Draft payload is internally coherent')
