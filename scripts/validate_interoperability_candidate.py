from pathlib import Path
import json, subprocess, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
for p in ['model/interoperability/interoperability-profile.yaml','model/recognition/recognition-profile.yaml','model/assurance/calibration-baseline.yaml','evidence/adversarial/event-01.yaml']:
    yaml.safe_load((ROOT/p).read_text())
cp=subprocess.run([sys.executable,str(ROOT/'interop/harness.py')],cwd=ROOT,capture_output=True,text=True)
if cp.returncode: print(cp.stdout); print(cp.stderr); raise SystemExit(cp.returncode)
results=json.loads(cp.stdout)
assert len(results)>=5 and all(x['pass'] for x in results)
out={'schema_version':'1.0','event_id':'INT-EVT-001','status':'passed-internal-cross-codebase','results':results,'limitations':['Implementation B is independently coded within this repository, not independently operated by an external team.']}
(ROOT/'evidence/interoperability').mkdir(parents=True,exist_ok=True)
(ROOT/'evidence/interoperability/event-01-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(f"Candidate interoperability validation: PASS ({len(results)} bidirectional semantic cases)")
