from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, yaml

ROOT = Path(__file__).resolve().parents[3]

def _now(): return datetime.now(timezone.utc).isoformat()

def load_yaml(path):
    return yaml.safe_load((ROOT / path).read_text(encoding='utf-8'))

class LifecycleController:
    def __init__(self):
        self.model = load_yaml('model/operations/provider-lifecycle.yaml')
        self.transitions = {t['id']: t for t in self.model['transitions']}
    def transition(self, current, transition_id, acting_role, evidence):
        t=self.transitions[transition_id]
        if t['from'] != current: raise ValueError('INVALID_SOURCE_STATE')
        if t['decision_role'] != acting_role: raise PermissionError('UNAUTHORISED_DECISION_ROLE')
        missing=[e for e in t.get('evidence',[]) if e not in evidence]
        if missing: raise ValueError('MISSING_REQUIRED_EVIDENCE:'+','.join(missing))
        return {'transition_id':transition_id,'from':current,'to':t['to'],'decision_role':acting_role,'evidence':sorted(evidence),'effective_at':_now()}

class PolicyEvaluator:
    def evaluate(self, *, actor, provider_status, authority, action, at_time):
        reasons=[]
        if provider_status != 'active': reasons.append('PROVIDER_NOT_ACTIVE')
        if action not in authority.get('scope',[]): reasons.append('AUTHORITY_SCOPE_MISMATCH')
        if authority.get('revoked',False): reasons.append('AUTHORITY_REVOKED')
        if not (authority.get('not_before') <= at_time <= authority.get('not_after')): reasons.append('AUTHORITY_OUTSIDE_VALID_TIME')
        decision='permit' if not reasons else 'deny'
        payload={'actor':actor,'action':action,'decision':decision,'reason_codes':reasons,'provider_status':provider_status,'authority_id':authority.get('id'),'evaluated_at':at_time,'requirements':['ONDTF-AUT-001','ONDTF-AUT-002','ONDTF-AUT-003']}
        canon=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
        payload['receipt_id']='RCP-'+hashlib.sha256(canon).hexdigest()[:16].upper()
        return payload
