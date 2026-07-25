#!/usr/bin/env python3
from pathlib import Path
import json, re, subprocess, sys, yaml
root=Path(__file__).resolve().parents[1]
terms_dir=root/'model/terminology/terms'; errors=[]; records={}; aliases={}
controlled=yaml.safe_load((root/'model/terminology/schema/controlled-vocabularies.yaml').read_text())
required={'schema_version','id','term','definition','status','classification','normative','owner','lifecycle'}
for p in sorted(terms_dir.glob('*.yaml')):
    try: r=yaml.safe_load(p.read_text()) or {}
    except Exception as e: errors.append(f'{p.relative_to(root)} invalid YAML: {e}'); continue
    missing=required-set(r)
    if missing: errors.append(f'{p.relative_to(root)} missing: {sorted(missing)}')
    id_=r.get('id','')
    if p.stem!=id_: errors.append(f'{p.relative_to(root)} filename does not match id {id_!r}')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',id_): errors.append(f'{p.relative_to(root)} invalid id')
    if id_ in records: errors.append(f'duplicate term id: {id_}')
    records[id_]=r
    if r.get('status') not in controlled['statuses']: errors.append(f'{id_}: invalid status')
    if r.get('classification') not in controlled['classifications']: errors.append(f'{id_}: invalid classification')
    if not isinstance(r.get('normative'),bool): errors.append(f'{id_}: normative must be boolean')
    if len(str(r.get('definition',''))) < 20: errors.append(f'{id_}: definition too short')
    for a in r.get('aliases',[]):
        key=a.casefold()
        if key in aliases and aliases[key]!=id_: errors.append(f"alias {a!r} used by {aliases[key]} and {id_}")
        aliases[key]=id_
for id_,r in records.items():
    for target in r.get('see_also',[]):
        if target not in records: errors.append(f'{id_}: unknown see_also target {target}')
    for m in r.get('external_mappings',[]):
        if m.get('relationship') not in controlled['mapping_relationships']: errors.append(f'{id_}: invalid mapping relationship')
        if not m.get('version'): errors.append(f'{id_}: external mapping lacks version')
    lp=r.get('lifecycle') or {}
    if lp.get('review_status') not in controlled['review_statuses']: errors.append(f'{id_}: invalid lifecycle review_status')
    page=root/f'docs/terminology/terms/{id_}.md'
    if not page.exists(): errors.append(f'{id_}: missing published term page')
inv=yaml.safe_load((root/'model/terminology/term-inventory.yaml').read_text())
if inv.get('term_count')!=len(records): errors.append('term inventory count does not match records')
if {x['id'] for x in inv.get('terms',[])}!=set(records): errors.append('term inventory identifiers do not match records')
# Rebuild and require deterministic artefacts to remain tracked.
subprocess.run([sys.executable,str(root/'scripts/build_terminology.py')],check=True)
for f in ['ondtf-glossary.json','ondtf-glossary.jsonld','term-inventory.json','ctwg-crosswalk.json','terminology-quality-report.json','artifact-manifest.json']:
    try: json.loads((root/'artifacts/terminology'/f).read_text())
    except Exception as e: errors.append(f'artifacts/terminology/{f} invalid JSON: {e}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'ONDTF terminology validation passed: {len(records)} governed terms checked.')
