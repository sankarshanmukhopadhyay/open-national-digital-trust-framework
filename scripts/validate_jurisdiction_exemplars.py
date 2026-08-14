#!/usr/bin/env python3
from pathlib import Path
import sys,yaml
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'examples'/'jurisdiction-exemplars'
EXPECTED={'australia-digital-id','uk-dvs','singapore-singpass','eudi-wallet'}
REQ={r.get('id') for r in yaml.safe_load((ROOT/'model/normative/requirement-catalogue.yaml').read_text()).get('requirements',[])}
errors=[]
if not (BASE/'index.md').exists(): errors.append('missing jurisdiction exemplar index')
found={p.name for p in BASE.iterdir() if p.is_dir()} if BASE.exists() else set()
if found!=EXPECTED: errors.append(f'exemplar set mismatch: expected {sorted(EXPECTED)}, found {sorted(found)}')
for slug in sorted(EXPECTED):
 p=BASE/slug
 for rel in ['index.md','governance-and-lifecycle.md','assurance-rights-and-conformance.md','source-and-provenance.md','model/profile.yaml','model/authority-roles.yaml','model/lifecycle.yaml','model/scenarios.yaml','model/ondtf-mapping.yaml','model/source-register.yaml']:
  if not (p/rel).exists(): errors.append(f'{slug}: missing {rel}')
 if not (p/'model/source-register.yaml').exists(): continue
 src=yaml.safe_load((p/'model/source-register.yaml').read_text())
 if src.get('source_cutoff')!='2026-08-14': errors.append(f'{slug}: unexpected source cut-off')
 sources=src.get('sources',[])
 if len(sources)<5: errors.append(f'{slug}: fewer than 5 authoritative sources')
 for s in sources:
  if not str(s.get('url','')).startswith('https://'): errors.append(f'{slug}: non-https source {s.get("key")}')
 mp=yaml.safe_load((p/'model/ondtf-mapping.yaml').read_text())
 if mp.get('normative_effect')!='none': errors.append(f'{slug}: exemplar acquired normative effect')
 if not mp.get('portability_rule'): errors.append(f'{slug}: missing portability rule')
 for m in mp.get('mappings',[]):
  for rid in m.get('ondtf_requirements',[]):
   if rid not in REQ: errors.append(f'{slug}: unknown requirement {rid}')
 life=yaml.safe_load((p/'model/lifecycle.yaml').read_text())
 if life.get('mapping_status')!='analytical-inference': errors.append(f'{slug}: lifecycle not marked analytical inference')
 if any(st.get('external_state_label_asserted') is not False for st in life.get('states',[])): errors.append(f'{slug}: lifecycle state presented as external canonical state')
 sc=yaml.safe_load((p/'model/scenarios.yaml').read_text())
 if len(sc.get('scenarios',[]))<7: errors.append(f'{slug}: scenario corpus too small')
 text=(p/'index.md').read_text()+ (p/'source-and-provenance.md').read_text()
 if 'not legal advice' not in text.lower() and 'not legal' not in text.lower(): errors.append(f'{slug}: missing legal/interpretive disclaimer')
if errors:
 print('Jurisdiction exemplar validation: FAIL')
 for e in errors: print(' -',e)
 sys.exit(1)
print('Jurisdiction exemplar validation: PASS')
print('Exemplars:',len(EXPECTED))
print('Authoritative sources:',sum(len(yaml.safe_load((BASE/s/'model/source-register.yaml').read_text()).get('sources',[])) for s in EXPECTED))
print('Scenario cases:',sum(len(yaml.safe_load((BASE/s/'model/scenarios.yaml').read_text()).get('scenarios',[])) for s in EXPECTED))
