#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
root=Path(__file__).resolve().parents[1]
errors=[]
def load(rel):
 p=root/rel
 if not p.exists(): errors.append(f'Missing {rel}'); return {}
 try:
  return json.loads(p.read_text()) if p.suffix=='.json' else (yaml.safe_load(p.read_text()) or {})
 except Exception as e: errors.append(f'{rel}: parse failure: {e}'); return {}
roles=load('model/governance/institutional-role-catalogue.yaml')
role_ids={x.get('id') for x in roles.get('roles',[]) if x.get('id')}
life=load('model/operations/provider-lifecycle.yaml')
states={x.get('id') for x in life.get('states',[]) if x.get('id')}
for t in life.get('transitions',[]):
 for f in ('id','from','to','decision_role','trigger','evidence'):
  if not t.get(f): errors.append(f"Lifecycle transition {t.get('id')}: missing {f}")
 if t.get('from') not in states or t.get('to') not in states: errors.append(f"{t.get('id')}: unknown state")
 if t.get('decision_role') not in role_ids: errors.append(f"{t.get('id')}: unknown role")
scheme=load('model/conformance/assessment-scheme.yaml').get('scheme',{})
for f in ('id','owner_role','administrator_role','assessment_roles','decision_role','accreditation_role','claim_layers','assessment_methods','required_controls','construction_mapping'):
 if not scheme.get(f): errors.append(f'Assessment scheme missing {f}')
for f in ('owner_role','administrator_role','decision_role','accreditation_role'):
 if scheme.get(f) not in role_ids: errors.append(f'Assessment scheme unknown role {scheme.get(f)}')
for r in scheme.get('assessment_roles',[]):
 if r not in role_ids: errors.append(f'Assessment scheme unknown assessment role {r}')
for rel in ['model/conformance/conformance-claim.schema.json','model/conformance/assessment-record.schema.json','model/conformance/nonconformity.schema.json']:
 load(rel)
contract=load('model/adoption/construction-input-contract.yaml')
ids=[x.get('id') for x in contract.get('decision_points',[])]
if len(ids)!=len(set(ids)): errors.append('Construction decision IDs must be unique')
for d in contract.get('decision_points',[]):
 for f in ('id','section','prompt','response_type','required','maps_to','review'):
  if f not in d: errors.append(f"{d.get('id')}: missing {f}")
required_docs=['docs/operations/provider-lifecycle.md','docs/operations/service-lifecycle.md','docs/operations/admission-and-onboarding.md','docs/operations/material-change-management.md','docs/operations/monitoring-and-surveillance.md','docs/operations/suspension-restriction-and-withdrawal.md','docs/operations/orderly-exit-and-continuity.md','docs/operations/trustmark-and-status-publication.md','docs/conformance/index.md','docs/conformance/conformance-claim-types.md','docs/conformance/assessment-scheme.md','docs/conformance/assessor-competence.md','docs/conformance/evidence-requirements.md','docs/conformance/assessment-decision.md','docs/conformance/certificate-and-claim-lifecycle.md','docs/conformance/surveillance-and-reassessment.md','docs/conformance/nonconformity-and-remediation.md','docs/conformance/public-conformance-register.md','docs/conformance/appeals-and-complaints.md','docs/adoption/guided-construction-readiness.md']
for rel in required_docs:
 if not (root/rel).exists(): errors.append(f'Missing required page {rel}')
if errors:
 print('\n'.join(errors)); sys.exit(1)
print(f"Operations/conformance validation passed: {len(states)} lifecycle states, {len(life.get('transitions',[]))} transitions and {len(contract.get('decision_points',[]))} guided-construction inputs checked.")
