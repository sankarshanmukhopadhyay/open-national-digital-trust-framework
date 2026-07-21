#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
required=['README.md','LICENSE','ROADMAP.md','GOVERNANCE.md','CONTRIBUTING.md','SECURITY.md','CHANGELOG.md','RELEASE_NOTES.md','_config.yml','docs/index.md','profiles/index.md']
for f in required:
    if not (root/f).exists(): errors.append(f'Missing required file: {f}')
for p in list(root.rglob('*.md')):
    text=p.read_text(encoding='utf-8')
    if '```mermaid' in text and text.count('```mermaid') > text.count('```')//2:
        errors.append(f'Possibly unclosed Mermaid block: {p.relative_to(root)}')
    for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', text):
        target=m.group(1).split('#')[0]
        if not target or '://' in target or target.startswith('mailto:') or target.startswith('#'): continue
        resolved=(p.parent/target).resolve()
        if not resolved.exists(): errors.append(f'Broken local link in {p.relative_to(root)}: {target}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('ONDTF repository validation passed.')
