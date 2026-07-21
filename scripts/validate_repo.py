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
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'ONDTF repository validation passed: {len(pages)} published Markdown pages checked.')
