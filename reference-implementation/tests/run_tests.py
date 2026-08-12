from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'reference-implementation'/'src'))
from ondtf_ref.core import LifecycleController, PolicyEvaluator

lc=LifecycleController()
r=lc.transition('active','PLT-008','ROLE-SA',{'suspension_decision'})
assert r['to']=='suspended'
try:
    lc.transition('active','PLT-008','ROLE-FA',{'suspension_decision'})
    raise AssertionError('unauthorised transition accepted')
except PermissionError: pass

p=PolicyEvaluator(); auth={'id':'AUTH-1','scope':['book'],'revoked':False,'not_before':'2026-01-01T00:00:00Z','not_after':'2026-12-31T23:59:59Z'}
assert p.evaluate(actor='agent-a',provider_status='active',authority=auth,action='book',at_time='2026-08-12T12:00:00Z')['decision']=='permit'
assert p.evaluate(actor='agent-a',provider_status='suspended',authority=auth,action='book',at_time='2026-08-12T12:00:00Z')['decision']=='deny'
auth['revoked']=True
assert 'AUTHORITY_REVOKED' in p.evaluate(actor='agent-a',provider_status='active',authority=auth,action='book',at_time='2026-08-12T12:00:00Z')['reason_codes']
print('Reference implementation tests: PASS (5 assertions)')
