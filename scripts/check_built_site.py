#!/usr/bin/env python3
from pathlib import Path
import sys
site=Path('_site')
errors=[]
if not site.exists(): errors.append('_site does not exist')
html=list(site.rglob('*.html')) if site.exists() else []
if not html: errors.append('No generated HTML pages found')
mermaid_pages=0
for p in html:
    text=p.read_text(encoding='utf-8',errors='ignore')
    if '```mermaid' in text: errors.append(f'Unprocessed Mermaid fence in {p}')
    if 'language-mermaid' in text or 'class="mermaid"' in text:
        mermaid_pages += 1
        if 'mermaid.min.js' not in text:
            errors.append(f'Mermaid runtime missing from {p}')
    if 'Diagram could not be rendered.' in text:
        errors.append(f'Legacy Mermaid fallback text present in {p}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'Built-site check passed: {len(html)} HTML files inspected; {mermaid_pages} pages contain Mermaid source.')
