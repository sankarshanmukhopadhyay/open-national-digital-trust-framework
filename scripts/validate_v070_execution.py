from pathlib import Path
import json, subprocess, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
req=yaml.safe_load((ROOT/'model/normative/requirement-catalogue.yaml').read_text())
reqids={x['id'] for x in req['requirements']}
ass=yaml.safe_load((ROOT/'conformance/assertions.yaml').read_text())
for a in ass['assertions']:
    assert a['requirement'] in reqids, f"Unknown requirement {a['requirement']}"
    assert a['class'] in {'machine-executable','assessor-verifiable','judgement-dependent'}
evd=yaml.safe_load((ROOT/'model/evidence/evidence-inventory.yaml').read_text())
assert len({x['id'] for x in evd['records']})==len(evd['records'])
subprocess.run([sys.executable,str(ROOT/'reference-implementation/tests/run_tests.py')],check=True,cwd=ROOT)
print(f"v0.7 execution validation: PASS ({len(ass['assertions'])} assertions, {len(evd['records'])} evidence records)")
