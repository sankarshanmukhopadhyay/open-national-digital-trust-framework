#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml
root=Path(__file__).resolve().parents[1]
errors=[]
version=(root/'VERSION').read_text().strip()
if version!='0.5.0': errors.append(f'VERSION is {version}, expected 0.5.0')
for f in ['PROJECT-STATUS.yaml','CITATION.cff','model/releases/v0.5.0.yaml','release/RELEASE-NOTES-v0.5.0.md','release/MANIFEST-v0.5.0.md','release/CHECKLIST-v0.5.0.md','release/DOCUMENT-INVENTORY-v0.5.0.md','docs/project/foundational-principles.md','docs/project/capability-matrix.md']:
    if not (root/f).exists(): errors.append(f'Missing {f}')
for f in ['PROJECT-STATUS.yaml','CITATION.cff','model/releases/v0.5.0.yaml']:
    try: yaml.safe_load((root/f).read_text())
    except Exception as e: errors.append(f'Invalid YAML {f}: {e}')
readme=(root/'README.md').read_text()
if 'v0.5.0' not in readme or 'Feature Complete Draft' not in readme: errors.append('README release status not updated')
if errors:
    print('Release validation failed:')
    for e in errors: print(f'- {e}')
    sys.exit(1)
print('Release validation passed: v0.5.0 Feature Complete Draft payload is internally coherent')
