from __future__ import annotations
from pathlib import Path
import hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'reference-implementation/src'))
sys.path.insert(0,str(ROOT/'implementations/implementation-b'))
from ondtf_ref.core import PolicyEvaluator
from engine import decide as decide_b

def record(**overrides):
    payload={'provider_state':'active','revoked':False,'observed_age_seconds':10,'action':'verify','scope':['verify']}
    payload.update(overrides)
    base={'record_id':'INT-REC-001','record_type':'authority','schema_version':'1.0','profile_id':'IPR-001','producer':'implementation-A','issued_at':'2026-08-14T00:00:00Z','payload':payload}
    digest=hashlib.sha256(json.dumps(base,sort_keys=True).encode()).hexdigest()
    base['integrity']={'mechanism':'sha256-fixture','value':digest}; return base

def decide_a(r):
    p=r['payload']; auth={'id':'AUTH-1','scope':p.get('scope',[]),'revoked':p.get('revoked',False),'not_before':'2026-01-01T00:00:00Z','not_after':'2027-01-01T00:00:00Z'}
    result=PolicyEvaluator().evaluate(actor='implementation-b',provider_status=p.get('provider_state'),authority=auth,action=p.get('action'),at_time='2026-08-14T00:00:00Z')
    if p.get('observed_age_seconds',0)>300:
        result['decision']='deny'; result['reason_codes']=sorted(set(result['reason_codes']+['STALE_STATUS']))
    return result

def run():
    cases=[
      ('INT-001','positive',record(),'permit'),
      ('INT-002','suspended-provider',record(provider_state='suspended'),'deny'),
      ('INT-003','revoked-authority',record(revoked=True),'deny'),
      ('INT-004','stale-status',record(observed_age_seconds=999),'deny'),
      ('INT-005','scope-mismatch',record(action='admin'),'deny')]
    out=[]
    for cid,name,r,expected in cases:
        a=decide_a(r); b=decide_b(r,now='2026-08-14T00:00:00Z')
        ok=a['decision']==expected and b['decision']==expected
        out.append({'id':cid,'scenario':name,'expected':expected,'implementation_a':a['decision'],'implementation_b':b['decision'],'pass':ok})
    return out
if __name__=='__main__':
    results=run(); print(json.dumps(results,indent=2)); raise SystemExit(0 if all(x['pass'] for x in results) else 1)
