#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

root = Path(__file__).resolve().parents[1]
errors = []

readiness_path = root / 'model/project/v0.5-readiness.yaml'
try:
    readiness = yaml.safe_load(readiness_path.read_text(encoding='utf-8')) or {}
except Exception as exc:
    errors.append(f'Invalid readiness record: {exc}')
    readiness = {}

for key in ('known_issues_register', 'readiness_checklist', 'integration_review'):
    target = readiness.get(key)
    if not target:
        errors.append(f'Missing readiness field: {key}')
    elif not (root / target).exists():
        errors.append(f'Readiness field {key} points to missing file: {target}')

for domain, status in (readiness.get('capability_domains') or {}).items():
    if status not in {'complete', 'complete_for_draft'}:
        errors.append(f'Capability domain is not complete for draft: {domain}={status}')

# Every citation to the central register must resolve to a registered identifier.
try:
    register = yaml.safe_load((root/'model/references/standards-register.yaml').read_text(encoding='utf-8')) or {}
    ids = {entry['id'] for entry in register.get('references', [])}
except Exception as exc:
    errors.append(f'Unable to read standards register: {exc}')
    ids = set()

citation_re = re.compile(r'references(?:\.md|\.html)?#ref-([A-Za-z0-9._-]+)')
markdown_files = list((root/'docs').rglob('*.md')) + list((root/'profiles').rglob('*.md'))
for page in markdown_files:
    text = page.read_text(encoding='utf-8')
    for cited in citation_re.findall(text):
        if cited not in ids:
            errors.append(f'Unknown standards citation {cited} in {page.relative_to(root)}')

# The generated standards table depends on stable row identifiers and a responsive wrapper.
refs_page = (root/'docs/standards/references.md').read_text(encoding='utf-8')
for marker in ('class="ondtf-table-scroll"', 'class="ondtf-reference-table"', 'id="ref-{{ ref.id }}"'):
    if marker not in refs_page:
        errors.append(f'Standards table is missing required marker: {marker}')

# Every project integration page must be discoverable from both the section index and site map.
required_project_pages = [
    'v0.5-readiness-checklist.md',
    'integration-review.md',
    'unresolved-issues.md',
]
project_index = (root/'docs/project/index.md').read_text(encoding='utf-8')
site_map = (root/'docs/site-map.md').read_text(encoding='utf-8')
for name in required_project_pages:
    if name not in project_index:
        errors.append(f'Project index does not link to {name}')
    html_name = name[:-3] + '.html'
    if html_name not in site_map:
        errors.append(f'Site map does not link to {html_name}')

# Changelog must begin with a single Unreleased section after the title.
changelog = (root/'CHANGELOG.md').read_text(encoding='utf-8')
if not re.match(r'# Changelog\s+## \[Unreleased\]', changelog):
    errors.append('CHANGELOG.md must begin with a single ## [Unreleased] section')
if changelog.count('## [Unreleased]') != 1:
    errors.append('CHANGELOG.md must contain exactly one ## [Unreleased] section')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'Integration validation passed: {len(markdown_files)} published pages and {len(ids)} registered references checked.')
