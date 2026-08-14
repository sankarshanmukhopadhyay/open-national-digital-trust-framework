from pathlib import Path
import json, subprocess, sys, yaml
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
req=yaml.safe_load((ROOT/'model/normative/requirement-catalogue.yaml').read_text())
reqids={r['id'] for r in req['requirements']}
assert req['version']=='0.9.0-candidate' and req['status']=='active'
assert all(r['status']=='active' for r in req['requirements'])
ass=yaml.safe_load((ROOT/'conformance/candidate-assertions.yaml').read_text())
coverage=yaml.safe_load((ROOT/'model/conformance/candidate-coverage.yaml').read_text())
assert {a['requirement'] for a in ass['assertions']}==reqids, 'candidate assertions do not cover every requirement'
assert {c['requirement'] for c in coverage['coverage']}==reqids, 'coverage matrix incomplete'
assert all(c['coverage_status']=='covered' for c in coverage['coverage'])
classes=yaml.safe_load((ROOT/'model/conformance/conformance-classes.yaml').read_text())
classids={c['id'] for c in classes['classes']}
assert all(a['conformance_class'] in classids for a in ass['assertions'])
manifest=yaml.safe_load((ROOT/'model/project/normative-document-manifest.yaml').read_text())
assert manifest['freeze_status']=='candidate'
for a in manifest['artefacts']:
    assert (ROOT/a['path']).exists(), f"missing candidate artefact {a['path']}"
# two construction responses validate against schema and complete current question set
schema=json.loads((ROOT/'model/adoption/construction-response.schema.json').read_text())
validator=Draft202012Validator(schema)
questions=yaml.safe_load((ROOT/'model/adoption/question-catalogue.yaml').read_text())['questions']
qids={q['id'] for q in questions}
for rel in ['examples/worked-profile/model/construction-response.json','examples/candidate-profile-b/model/construction-response.json']:
    obj=json.loads((ROOT/rel).read_text()); errs=list(validator.iter_errors(obj)); assert not errs, f"{rel}: {errs[0].message if errs else ''}"
    got={r['question_id'] for r in obj['responses']}; assert got==qids, f'{rel}: question coverage mismatch'
# interoperability evidence must remain green
subprocess.run([sys.executable,str(ROOT/'scripts/validate_interoperability_candidate.py')],cwd=ROOT,check=True)
print(f"Candidate specification validation: PASS ({len(reqids)} requirements, {len(ass['assertions'])} assertions, {len(classids)} conformance classes, 2 construction packages)")
