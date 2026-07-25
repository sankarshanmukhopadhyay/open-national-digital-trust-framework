#!/usr/bin/env python3
from pathlib import Path
import json, yaml, hashlib
root=Path(__file__).resolve().parents[1]
source=root/'model/terminology/terms'; out=root/'artifacts/terminology'; out.mkdir(parents=True,exist_ok=True)
records=[yaml.safe_load(p.read_text(encoding='utf-8')) for p in sorted(source.glob('*.yaml'))]
payload={'schema_version':'1.0','framework':'ONDTF','framework_version':(root/'VERSION').read_text().strip(),'authority':'ONDTF','terms':records}
json_text=json.dumps(payload,indent=2,ensure_ascii=False)+'\n'
(out/'ondtf-glossary.json').write_text(json_text,encoding='utf-8')
context={'@context':{'ondtf':'https://sankarshanmukhopadhyay.github.io/open-national-digital-trust-framework/terms/','id':'@id','type':'@type','term':'http://www.w3.org/2004/02/skos/core#prefLabel','definition':'http://www.w3.org/2004/02/skos/core#definition','aliases':'http://www.w3.org/2004/02/skos/core#altLabel','see_also':{'@id':'http://www.w3.org/2004/02/skos/core#related','@type':'@id'}},'@graph':[{'id':f"ondtf:{r['id']}",'type':'http://www.w3.org/2004/02/skos/core#Concept','term':r['term'],'definition':r['definition'],'aliases':r.get('aliases',[]),'see_also':[f"ondtf:{x}" for x in r.get('see_also',[])]} for r in records]}
(out/'ondtf-glossary.jsonld').write_text(json.dumps(context,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
inv=yaml.safe_load((root/'model/terminology/term-inventory.yaml').read_text())
(out/'term-inventory.json').write_text(json.dumps(inv,indent=2)+'\n',encoding='utf-8')
cross=yaml.safe_load((root/'model/terminology/external-crosswalks/ctwg.yaml').read_text())
(out/'ctwg-crosswalk.json').write_text(json.dumps(cross,indent=2)+'\n',encoding='utf-8')
quality={'schema_version':'1.0','term_count':len(records),'active_terms':sum(r['status']=='active' for r in records),'normative_terms':sum(bool(r['normative']) for r in records),'terms_with_external_mappings':sum(bool(r.get('external_mappings')) for r in records),'terms_with_related_terms':sum(bool(r.get('see_also')) for r in records),'structural_checks':'Run scripts/validate_terminology.py for authoritative results.','semantic_assurance_limit':'Automated checks do not establish semantic equivalence or jurisdictional neutrality.'}
(out/'terminology-quality-report.json').write_text(json.dumps(quality,indent=2)+'\n',encoding='utf-8')
files=sorted(p for p in out.glob('*') if p.name!='artifact-manifest.json')
manifest={'schema_version':'1.0','framework_version':payload['framework_version'],'artifacts':[{'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
(out/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(f'Generated {len(files)+1} terminology artefacts from {len(records)} terms.')
