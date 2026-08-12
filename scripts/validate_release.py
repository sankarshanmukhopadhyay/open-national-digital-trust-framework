#!/usr/bin/env python3
from pathlib import Path
import sys,yaml
root=Path(__file__).resolve().parents[1]; errors=[]
version=(root/'VERSION').read_text().strip()
if version!='0.7.0': errors.append(f'VERSION is {version}, expected 0.7.0')
required=['scripts/validate_release_integrity.py','scripts/validate_v070_execution.py','scripts/validate_identifier_registry.py','PROJECT-STATUS.yaml','CITATION.cff','model/releases/v0.7.0.yaml','release/RELEASE-NOTES-v0.7.0.md','release/MANIFEST-v0.7.0.md','release/CHECKLIST-v0.7.0.md','release/EVIDENCE-INVENTORY-v0.7.0.md','release/REQUIREMENTS-INVENTORY-v0.7.0.md','release/DEVIATION-REGISTER-v0.7.0.md','release/VALIDATION-NOTES-v0.7.0.md','docs/project/v0.7-readiness-checklist.md']
for f in required:
 if not (root/f).exists(): errors.append(f'Missing {f}')
for f in ['PROJECT-STATUS.yaml','CITATION.cff','model/releases/v0.7.0.yaml']:
 try: yaml.safe_load((root/f).read_text())
 except Exception as e: errors.append(f'Invalid YAML {f}: {e}')
readme=(root/'README.md').read_text()
if 'v0.7.0' not in readme or 'Implementation and Evaluation Draft' not in readme: errors.append('README release status not updated')
if errors:
 print('Release validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print('Release validation passed: v0.7.0 Implementation and Evaluation Draft payload is internally coherent')
