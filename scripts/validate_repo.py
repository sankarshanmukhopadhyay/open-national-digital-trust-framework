#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml, json
root=Path(__file__).resolve().parents[1]
errors=[]
required=['README.md','LICENSE','ROADMAP.md','GOVERNANCE.md','CONTRIBUTING.md','SECURITY.md','CHANGELOG.md','RELEASE_NOTES.md','_config.yml','docs/index.md','docs/site-map.md','profiles/index.md','VERSION','PROJECT-STATUS.yaml']
for f in required:
    if not (root/f).exists(): errors.append(f'Missing required file: {f}')
pages=[]
for p in list((root/'docs').rglob('*.md'))+list((root/'profiles').rglob('*.md')):
    text=p.read_text(encoding='utf-8')
    pages.append(p)
    if not text.startswith('---\n'):
        errors.append(f'Missing front matter: {p.relative_to(root)}')
        fm={}
    else:
        end=text.find('\n---\n',4)
        if end < 0:
            errors.append(f'Unclosed front matter: {p.relative_to(root)}'); fm={}
        else:
            try:
                fm=yaml.safe_load(text[4:end]) or {}
                if not fm.get('title'): errors.append(f'Missing title in front matter: {p.relative_to(root)}')
            except Exception as e:
                errors.append(f'Invalid YAML front matter in {p.relative_to(root)}: {e}'); fm={}
    if text.count('```mermaid') != len(re.findall(r'```mermaid\s*\n.*?\n```', text, re.S)):
        errors.append(f'Unclosed or malformed Mermaid block: {p.relative_to(root)}')
    for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', text):
        target=m.group(1).split('#')[0]
        if not target or '://' in target or target.startswith(('mailto:','#')) or '{{' in target or '{%' in target: continue
        resolved=(p.parent/target).resolve()
        if not resolved.exists(): errors.append(f'Broken local link in {p.relative_to(root)}: {target}')
for jp in list((root/'bindings').rglob('*.json')):
    try: json.loads(jp.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'Invalid JSON {jp.relative_to(root)}: {e}')
for yp in list((root/'governance').rglob('*.yaml'))+list((root/'model').rglob('*.yaml'))+[root/'data/dependencies.yaml',root/'PROJECT-STATUS.yaml']:
    try: yaml.safe_load(yp.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'Invalid YAML {yp.relative_to(root)}: {e}')

# Navigation integrity: nav_order must be unique within each Just-the-Docs parent.
nav_by_parent={}
for p in pages:
    text=p.read_text(encoding='utf-8')
    m=re.search(r'^---\n(.*?)\n---\n',text,re.S)
    if not m: continue
    fm=yaml.safe_load(m.group(1)) or {}
    parent=fm.get('parent'); order=fm.get('nav_order')
    if parent is not None and order is not None:
        nav_by_parent.setdefault(parent,{}).setdefault(order,[]).append(p.relative_to(root))
for parent,orders in nav_by_parent.items():
    for order,files in orders.items():
        if len(files)>1:
            errors.append(f"Duplicate nav_order {order} under parent '{parent}': "+', '.join(str(f) for f in files))

# Framework self-version consistency across all machine-readable declarations.
version_file=(root/'VERSION').read_text(encoding='utf-8').strip()
version_sources={'VERSION':version_file}
try:
    status=yaml.safe_load((root/'PROJECT-STATUS.yaml').read_text(encoding='utf-8')) or {}
    version_sources['PROJECT-STATUS.yaml:version']=str(status.get('version'))
except Exception:
    pass
try:
    citation=yaml.safe_load((root/'CITATION.cff').read_text(encoding='utf-8')) or {}
    version_sources['CITATION.cff:version']=str(citation.get('version'))
except Exception:
    pass
readme_match=re.search(r'version-v?([0-9]+\.[0-9]+\.[0-9]+)-',(root/'README.md').read_text(encoding='utf-8'))
if readme_match:
    version_sources['README.md:badge']=readme_match.group(1)
try:
    deps=yaml.safe_load((root/'data/dependencies.yaml').read_text(encoding='utf-8')) or {}
    fw_version=deps.get('framework',{}).get('version')
    if fw_version is not None:
        version_sources['data/dependencies.yaml:framework.version']=str(fw_version)
except Exception:
    pass
# Binding artefacts are independently versioned and may intentionally target an
# earlier ONDTF baseline. Validate their internal version/identifier coherence
# separately rather than requiring them to match the current repository release.
for jp in sorted((root/'bindings').rglob('*.json')):
    try:
        payload=json.loads(jp.read_text(encoding='utf-8'))
        ov=payload.get('ondtfVersion')
        identifier=payload.get('profileId') or payload.get('bindingId')
        if ov is not None and identifier is not None and not str(identifier).endswith(':'+str(ov)):
            errors.append(f'Binding identifier/version mismatch in {jp.relative_to(root)}: identifier={identifier}; ondtfVersion={ov}')
    except Exception:
        pass
distinct_versions=set(version_sources.values())
if len(distinct_versions)>1:
    detail='; '.join(f'{k}={v}' for k,v in version_sources.items())
    errors.append(f'ONDTF self-version mismatch across machine-readable declarations: {detail}')

# Decision register completeness: every published ADR must be registered.
adr_files=sorted((root/'docs/decisions').glob('0*-*.md'))
try:
    register=yaml.safe_load((root/'governance/decision-register.yaml').read_text(encoding='utf-8')) or {}
    registered_ids={d.get('id') for d in register.get('decisions',[])}
except Exception:
    registered_ids=set()
for af in adr_files:
    adr_id='ADR-'+af.name.split('-')[0]
    if adr_id not in registered_ids:
        errors.append(f'Published ADR not present in governance/decision-register.yaml: {adr_id} ({af.relative_to(root)})')

# Security-domain traceability: every declared domain must be referenced by at least one protected asset.
try:
    foundations=yaml.safe_load((root/'model/security/security-foundations.yaml').read_text(encoding='utf-8')) or {}
    declared_domains={d['id'] for d in foundations.get('domains',[])}
    protected=yaml.safe_load((root/'model/security/protected-assets.yaml').read_text(encoding='utf-8')) or {}
    referenced_domains=set()
    for asset in protected.get('assets',[]):
        referenced_domains.update(asset.get('domains',[]))
    for dom in sorted(declared_domains-referenced_domains):
        errors.append(f'Security domain {dom} is declared in security-foundations.yaml but has no protected-asset reference')
except FileNotFoundError:
    pass

if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'ONDTF repository validation passed: {len(pages)} published Markdown pages checked.')

# Sector standards validation is also run independently by the Makefile.
