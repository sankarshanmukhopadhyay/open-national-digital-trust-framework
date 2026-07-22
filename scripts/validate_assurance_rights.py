#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
root=Path(__file__).resolve().parents[1]
errors=[]
def load(rel):
 p=root/rel
 if not p.exists(): errors.append(f"Missing {rel}"); return {}
 try: return json.loads(p.read_text()) if p.suffix=='.json' else (yaml.safe_load(p.read_text()) or {})
 except Exception as e: errors.append(f"{rel}: parse failure: {e}"); return {}
dims=load('model/assurance/assurance-dimensions.yaml').get('dimensions',[])
dim_ids=[x.get('id') for x in dims]
if len(dim_ids)!=9 or len(dim_ids)!=len(set(dim_ids)): errors.append('Assurance dimensions must contain nine unique IDs')
levels=load('model/assurance/assurance-levels.yaml').get('levels',[])
if [x.get('id') for x in levels] != ['AL-0','AL-1','AL-2','AL-3']: errors.append('Assurance levels must define AL-0 through AL-3 in order')
load('model/assurance/assurance-claim.schema.json')
for rel in ['model/rights/challenge-record.schema.json','model/rights/appeal-record.schema.json','model/rights/remedy-record.schema.json','model/rights/accessibility-evidence.schema.json']:
 load(rel)
contract=load('model/adoption/construction-input-contract.yaml')
ids=[x.get('id') for x in contract.get('decision_points',[])]
for prefix,count in [('GFC-ASR-',5),('GFC-RGT-',5)]:
 found=[x for x in ids if isinstance(x,str) and x.startswith(prefix)]
 if len(found)!=count: errors.append(f'{prefix} expected {count} decision points, found {len(found)}')
required_docs=['docs/assurance/assurance-level-model.md','docs/assurance/identity-assurance.md','docs/assurance/authority-assurance.md','docs/assurance/delegation-assurance.md','docs/assurance/evidence-assurance.md','docs/assurance/execution-assurance.md','docs/assurance/status-freshness-assurance.md','docs/assurance/privacy-assurance.md','docs/assurance/remedy-readiness-assurance.md','docs/assurance/assurance-composition.md','docs/rights/affected-party-operating-model.md','docs/rights/notice-and-explanation.md','docs/rights/challenge-and-correction.md','docs/rights/appeal-and-independent-review.md','docs/rights/remedy-execution.md','docs/rights/accessibility-and-assisted-use.md','docs/rights/exclusion-and-alternative-channels.md','docs/rights/rights-evidence.md']
for rel in required_docs:
 if not (root/rel).exists(): errors.append(f'Missing required page {rel}')
# internal-only delivery terminology must not leak into repository content
for p in root.rglob('*'):
 if p.is_file() and '.git' not in p.parts and p.suffix.lower() in {'.md','.yaml','.yml','.json','.py','.txt'}:
  try: txt=p.read_text().lower()
  except: continue
  for term in tuple('commit ' + str(n) for n in (2,3,4)):
   if term in txt: errors.append(f'Internal delivery term {term!r} found in {p.relative_to(root)}')
if errors:
 print('\n'.join(errors)); sys.exit(1)
print(f'Assurance/rights validation passed: {len(dims)} dimensions, {len(levels)} levels and 10 guided-construction inputs checked.')
