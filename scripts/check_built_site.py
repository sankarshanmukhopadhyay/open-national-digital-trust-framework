#!/usr/bin/env python3
from pathlib import Path
import sys
site=Path('_site')
errors=[]
if not site.exists(): errors.append('_site does not exist')
html=list(site.rglob('*.html')) if site.exists() else []
if not html: errors.append('No generated HTML pages found')
for p in html:
    text=p.read_text(encoding='utf-8',errors='ignore')
    if '```mermaid' in text: errors.append(f'Unprocessed Mermaid fence in {p}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'Built-site check passed: {len(html)} HTML files inspected.')
