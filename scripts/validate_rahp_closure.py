from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(path):
    return yaml.safe_load((ROOT / path).read_text())

def require(condition, message):
    if not condition:
        raise AssertionError(message)

# ON-RH-01 legitimacy evidence beyond mandate.
lep = load_yaml('model/assurance/legitimacy-evidence-profile.yaml')
require(lep['id'] == 'LEP-001', 'LEP-001 missing')
dims = {d['name'] for d in lep['dimensions']}
require(dims == {'participation','proportionality','independent review','transparency','affected-party representation'}, 'LEP-001 dimensions incomplete')
require(lep['example']['formal_mandate'] == 'present', 'formal mandate example missing')
require(any(v == 'gap-identified' for k,v in lep['example'].items() if k != 'conclusion'), 'legitimacy gap exemplar missing')

# ON-RH-02 operational independence.
oi = load_yaml('model/governance/operational-independence-evidence.yaml')
require(oi['id'] == 'OIEP-001', 'OIEP-001 missing')
expected_oi = {'appointment authority','funding and control relationships','conflict-of-interest controls','recusal','decision override and remedial authority','publication obligations','structural dependence'}
require({t['dimension'] for t in oi['tests']} == expected_oi, 'operational independence tests incomplete')
require(oi['negative_scenario']['expected'] == 'fail-operational-independence', 'negative captive-review scenario missing')

# ON-RH-03 emergency authority negative vectors.
ngv = load_yaml('model/conformance/negative-governance-vectors.yaml')
require(ngv['id'] == 'NGV-001', 'NGV-001 missing')
required_cases = {'expired-emergency-authority','repeated-renewal-without-fresh-justification','scope-expansion','missing-independent-review','action-after-termination','retrospective-justification'}
require({v['case'] for v in ngv['vectors']} == required_cases, 'emergency negative cases incomplete')
require(all(v['requirement'] == 'ONDTF-GOV-006' and v['expected'] == 'nonconformant' for v in ngv['vectors']), 'emergency vectors must deterministically fail')

# ON-RH-04 recognition ceiling/lifecycle.
rec = load_yaml('model/recognition/recognition-profile.yaml')
for field in ('scope','equivalence','assurance_ceiling','evidence_basis','validity','lifecycle','weakest_link_rule'):
    require(field in rec, f'recognition field missing: {field}')
require(rec['assurance_ceiling']['excluded_claims'], 'recognition exclusions missing')
require(rec['validity']['expires_at'], 'recognition expiry missing')
require(rec['lifecycle']['revocation_state'] in {'not-revoked','revoked'}, 'recognition revocation state invalid')
require(any(e['result'] in {'conditionally-equivalent','not-equivalent','not-established'} for e in rec['equivalence']), 'partial/non-equivalence not represented')

# ON-RH-05 outcome-oriented remedy evidence.
remedy = json.loads((ROOT/'model/rights/remedy-record.schema.json').read_text())
for field in ('access_channel','eligibility_basis','interim_relief_requested','interim_relief_at','final_decision_at','consequential_state_changed','state_change_evidence','effectiveness_status'):
    require(field in remedy['properties'], f'remedy effectiveness field missing: {field}')
require('effective' in remedy['properties']['effectiveness_status']['enum'], 'effective remedy state missing')
require('ineffective' in remedy['properties']['effectiveness_status']['enum'], 'ineffective remedy state missing')

# ON-RH-06 portable semantics vectors.
psv = load_yaml('model/conformance/portable-semantics-vectors.yaml')
require(psv['id'] == 'PSV-001', 'PSV-001 missing')
require({v['semantic'] for v in psv['vectors']} == {'authority','delegation','evidence-freshness','suspension','revocation','remedy'}, 'portable semantic vectors incomplete')
require('divergence_from_core' in psv['profile_declaration_contract']['required_fields'], 'profile divergence declaration missing')

# Traceability and cross-repository boundary.
trace = load_yaml('model/rahp/combined-review-2026-08-16.yaml')
require({f['id'] for f in trace['findings']} == {f'ON-RH-0{i}' for i in range(1,7)}, 'RAHP finding trace incomplete')
require(all(f['status'] == 'addressed' and f['evidence'] for f in trace['findings']), 'all RAHP findings must have closure evidence')
require(trace['cross_repository_boundary']['duplicated_items'] == [], 'cross-repository findings must not be duplicated locally')

# Reader-facing pages must exist.
for page in [
    'docs/assurance/legitimacy-evidence.md',
    'docs/governance/operational-independence.md',
    'docs/conformance/negative-governance-vectors.md',
    'docs/interoperability/recognition-profile.md',
    'docs/interoperability/portable-semantics-vectors.md',
    'docs/rahp-follow-up-2026-08-16.md',
]:
    require((ROOT/page).exists(), f'documentation missing: {page}')

print('RAHP combined-review closure validation: PASS (ON-RH-01..ON-RH-06)')
