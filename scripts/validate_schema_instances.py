#!/usr/bin/env python3
"""Validate ONDTF JSON instances and positive/negative conformance fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'model/conformance/schema-instance-manifest.yaml'
REPORT=ROOT/'artifacts/conformance/schema-validation-report.json'

def load(path):
    with open(ROOT/path,encoding='utf-8') as f:
        return json.load(f) if str(path).endswith('.json') else yaml.safe_load(f)

def errors(schema, instance):
    v=Draft202012Validator(schema, format_checker=FormatChecker())
    return sorted(v.iter_errors(instance), key=lambda e: (list(e.path), list(e.schema_path)))

def main():
    manifest=load(MANIFEST.relative_to(ROOT))
    results=[]; failures=[]
    for item in manifest['validations']:
        schema=load(item['schema'])
        Draft202012Validator.check_schema(schema)
        for p in item.get('instances',[]):
            es=errors(schema,load(p)); ok=not es
            results.append({'schema':item['schema'],'instance':p,'expected':'pass','actual':'pass' if ok else 'fail','errors':[{'path':'/'.join(map(str,e.path)),'schema_path':'/'.join(map(str,e.schema_path)),'validator':e.validator,'message':e.message} for e in es]})
            if not ok: failures.append(f"Expected pass: {p}: {es[0].message}")
        for fixture in item.get('negative_fixtures',[]):
            es=errors(schema,load(fixture['instance']))
            validators={e.validator for e in es}
            ok=bool(es) and fixture['expected_validator'] in validators
            results.append({'schema':item['schema'],'instance':fixture['instance'],'expected':'fail','actual':'fail' if es else 'pass','expected_validator':fixture['expected_validator'],'observed_validators':sorted(str(x) for x in validators),'errors':[{'path':'/'.join(map(str,e.path)),'schema_path':'/'.join(map(str,e.schema_path)),'validator':e.validator,'message':e.message} for e in es]})
            if not ok: failures.append(f"Expected failure ({fixture['expected_validator']}): {fixture['instance']}")
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    report={'schema_version':'1.0','manifest':str(MANIFEST.relative_to(ROOT)),'summary':{'checks':len(results),'passed':len(results)-len(failures),'failed':len(failures)},'results':results}
    REPORT.write_text(json.dumps(report,indent=2)+"\n",encoding='utf-8')
    if failures:
        print('\n'.join(failures),file=sys.stderr); return 1
    print(f"Schema-instance validation passed: {len(results)} positive/negative checks across {len(manifest['validations'])} schemas.")
    return 0
if __name__=='__main__': raise SystemExit(main())
