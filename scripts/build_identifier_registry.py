from pathlib import Path
import re, yaml, json
ROOT=Path(__file__).resolve().parents[1]
PREFIXES=['ONDTF','ROLE','URI','IM','PLT','CT','ADV','JRN','CLAR','CAP','THR','CTL','SB','AST','THCAT','SEC','EPA','RS','INT','AS','AP','TA','TB','ADR','LIM','MPR','EVD','IPR','REC','EQV','CAL','CCL','NCP','REV','GFM']
PREFIX_ALT='|'.join(sorted(PREFIXES,key=len,reverse=True))
PAT=re.compile(rf'\b(?:(?:ONDTF)-[A-Z]{{3}}-\d{{3}}|(?:CT)-[A-Z]{{3}}-\d{{3}}|(?:JRN)-[A-Z]{{3}}-\d{{3}}|(?:{PREFIX_ALT})-\d{{2,4}}|ROLE-[A-Z0-9]+|IM-[A-Z]{{3}})\b')
EXCLUDE={Path('docs/information-model/identifier-registry.md'),Path('model/references/identifier-registry.yaml'),Path('assets/data/identifiers.json')}
found={}; labels={}
def rel(p): return p.relative_to(ROOT)
def walk(x):
    if isinstance(x,dict):
        ident=x.get('id')
        if isinstance(ident,str) and PAT.fullmatch(ident):
            labels.setdefault(ident,x.get('title') or x.get('name') or x.get('statement') or x.get('purpose') or '')
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts or rel(p) in EXCLUDE or p.suffix.lower() not in {'.md','.yaml','.yml','.json'}: continue
    try: txt=p.read_text(encoding='utf-8')
    except Exception: continue
    for ident in PAT.findall(txt): found.setdefault(ident,set()).add(str(rel(p)))
    if p.suffix.lower() in {'.yaml','.yml'}:
        try: walk(yaml.safe_load(txt))
        except Exception: pass
    if p.suffix.lower()=='.md':
        for line in txt.splitlines():
            if '|' not in line: continue
            cells=[c.strip().strip('`*[]') for c in line.strip().strip('|').split('|')]
            if not cells: continue
            for ident in PAT.findall(cells[0]):
                if len(cells)>1 and cells[1] and cells[1] not in {'---','Entity','Title','Name'}:
                    labels.setdefault(ident,re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',cells[1]))
reg=[{'id':i,'label':str(labels.get(i,'')),'sources':sorted(found[i])[:12]} for i in sorted(found)]
(ROOT/'model/references').mkdir(parents=True,exist_ok=True)
(ROOT/'model/references/identifier-registry.yaml').write_text(yaml.safe_dump({'schema_version':'1.0','generated':True,'identifier_classes':PREFIXES,'identifiers':reg},sort_keys=False,width=120),encoding='utf-8')
lines=['---','layout: default','title: Identifier Registry','parent: Information Architecture','nav_order: 7','---','','# Identifier registry','','This generated registry is the universal resolution surface for controlled ONDTF identifiers. Published pages automatically link recognised identifiers here; each entry provides a human label where the canonical sources expose one and points back to repository locations in which the identifier is defined or used.','','| Identifier | Meaning | Canonical/source locations |','|---|---|---|']
for x in reg:
    ident=x['id']; label=x['label'].replace('|','\\|') or 'Controlled ONDTF identifier'
    src='<br>'.join(f'`{s}`' for s in x['sources'][:4])
    lines.append(f'| <a id="{ident.lower()}"></a> **{ident}** | {label} | {src} |')
(ROOT/'docs/information-model/identifier-registry.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(ROOT/'assets/data').mkdir(parents=True,exist_ok=True)
(ROOT/'assets/data/identifiers.json').write_text(json.dumps({'identifiers':[x['id'] for x in reg]},indent=2),encoding='utf-8')
print(f'Identifier registry built: {len(reg)} identifiers across {len(PREFIXES)} controlled classes')
