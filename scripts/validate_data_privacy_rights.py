#!/usr/bin/env python3
from pathlib import Path
import sys,yaml
root=Path(__file__).resolve().parents[1]
required=[
'model/privacy/privacy-principles.yaml','model/privacy/privacy-controls.yaml','model/privacy/privacy-threats.yaml','model/privacy/privacy-impact-assessment-schema.yaml',
'model/data-security/classification-levels.yaml','model/data-security/retention-policy-schema.yaml','model/data-security/provenance-schema.yaml',
'model/rights/challenge-record-schema.yaml','model/rights/appeal-record-schema.yaml','model/rights/remedy-record-schema.yaml']
errors=[]; loaded={}
for rel in required:
 p=root/rel
 if not p.exists(): errors.append(f'Missing {rel}'); continue
 try: loaded[rel]=yaml.safe_load(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'Invalid YAML {rel}: {e}')
if not errors:
 principles={x['id'] for x in loaded['model/privacy/privacy-principles.yaml']['principles']}
 controls={x['id'] for x in loaded['model/privacy/privacy-controls.yaml']['controls']}
 for t in loaded['model/privacy/privacy-threats.yaml']['threats']:
  for r in t.get('principles',[]):
   if r not in principles: errors.append(f"{t['id']} unknown principle {r}")
  for r in t.get('control_refs',[]):
   if r not in controls: errors.append(f"{t['id']} unknown control {r}")
if errors:
 print('Data/privacy/rights validation failed:'); print('\n'.join(f'- {e}' for e in errors)); sys.exit(1)
print(f'Data/privacy/rights validation passed: {len(required)} machine-readable artefacts checked.')
