from __future__ import annotations

def decide(record, *, now, max_status_age=300):
    p=record.get('payload',{})
    if record.get('record_type')!='authority':
        return {'decision':'deny','reason_codes':['INCOMPLETE_EVIDENCE']}
    reasons=[]
    if p.get('provider_state')!='active': reasons.append('SUSPENDED_PROVIDER')
    if p.get('revoked') is True: reasons.append('REVOKED_AUTHORITY')
    if p.get('observed_age_seconds',0)>max_status_age: reasons.append('STALE_STATUS')
    if p.get('action') not in p.get('scope',[]): reasons.append('AUTHORITY_SCOPE_MISMATCH')
    return {'decision':'permit' if not reasons else 'deny','reason_codes':reasons,'implementation':'B'}
