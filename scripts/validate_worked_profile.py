#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
root=Path(__file__).resolve().parents[1]
errors=[]
def load(rel):
 p=root/rel
 if not p.exists(): errors.append(f"Missing {rel}"); return {}
 try: return json.loads(p.read_text()) if p.suffix=='.json' else (yaml.safe_load(p.read_text()) or {})
 except Exception as e: errors.append(f"{rel}: {e}"); return {}
q=load('model/adoption/question-catalogue.yaml')
g=load('model/adoption/completeness-gates.yaml')
pats={x['id'] for x in load('model/adoption/pattern-catalogue.yaml').get('patterns',[])}
r=load('examples/worked-profile/model/construction-response.json')
known={x['id']:x for x in q.get('questions',[])}
answers={x.get('question_id'):x for x in r.get('responses',[])}
allowed={'selected','inherited','profile_controlled','provisional','unresolved','review_required','not_applicable'}
for qid,item in known.items():
 dep=item.get('depends_on',[])
 applicable=True
 for d in dep:
  if answers.get(d['question'],{}).get('value') != d.get('equals'): applicable=False
 if item.get('required') and applicable and qid not in answers: errors.append(f'Missing applicable response {qid}')
for qid,a in answers.items():
 if qid not in known: errors.append(f'Unknown response {qid}')
 if a.get('state') not in allowed: errors.append(f'{qid}: invalid state')
 if not a.get('provenance',{}).get('authority_reference'): errors.append(f'{qid}: missing authority reference')
 val=a.get('value')
 if isinstance(val,dict) and 'pattern' in val and val['pattern'] not in pats: errors.append(f'{qid}: unknown pattern {val["pattern"]}')
for gate in g.get('stage_gates',[]):
 for qid in gate.get('required_questions',[]):
  if qid not in answers: errors.append(f'Stage {gate["stage"]}: missing {qid}')
required=['profile.yaml','roles.yaml','assurance.yaml','conformance.yaml','risk-register.yaml','decision-register.yaml','review-register.yaml']
for x in required: load('examples/worked-profile/model/'+x)
ass=load('examples/worked-profile/model/assurance.yaml')
if not {'authority','status_freshness','privacy','remedy_readiness'}.issubset(set(ass.get('critical_dimensions',[]))): errors.append('Critical assurance floors incomplete')
roles=load('examples/worked-profile/model/roles.yaml').get('roles',[])
if not any(x.get('id')=='remedy-body' and x.get('independent_from') for x in roles): errors.append('Independent remedy body missing')
reviews=load('examples/worked-profile/model/review-register.yaml')
if reviews.get('qualification',{}).get('status')!='required-before-deployment': errors.append('Authority qualification must block deployment')
if errors: print('\n'.join(errors)); sys.exit(1)
print(f"Worked profile validation passed: {len(answers)} guided responses, {len(q.get('stages',[]))} stages, {len(required)} governed model artefacts and one explicit deployment qualification checked.")
