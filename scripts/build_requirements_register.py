#!/usr/bin/env python3
"""Generate the human-readable ONDTF Requirements Register from canonical models."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / 'model/normative/requirement-catalogue.yaml'
ASSERTIONS = ROOT / 'conformance/candidate-assertions.yaml'
OUT = ROOT / 'docs/core-specification/requirements-register.md'

req_data = yaml.safe_load(REQ.read_text(encoding='utf-8')) or {}
assertion_data = yaml.safe_load(ASSERTIONS.read_text(encoding='utf-8')) or {}
assertions = assertion_data.get('assertions') or assertion_data.get('candidate_assertions') or []
by_req = {}
for item in assertions:
    rid = item.get('requirement')
    aid = item.get('id')
    if rid and aid:
        by_req.setdefault(rid, []).append(aid)

reqs = req_data.get('requirements') or []
by_domain = {}
for req in reqs:
    by_domain.setdefault(req.get('domain') or 'other', []).append(req)

lines = [
    '---',
    'layout: default',
    'title: Requirements Register',
    'parent: Core Specification',
    'nav_order: 4',
    '---',
    '',
    '# ONDTF Requirements Register',
    '',
    'The Requirements Register is the reader-facing resolution surface for every controlled `ONDTF-*` normative requirement. '
    'It is generated from `model/normative/requirement-catalogue.yaml`; the machine-readable catalogue remains canonical. '
    'Each stable anchor below is safe to cite from prose, tables, diagrams, examples and external review records.',
    '',
    'A requirement entry shows **what is required**, **where it applies**, **who is accountable and responsible**, '
    '**what evidence is expected**, and **which candidate conformance assertion evaluates it**.',
    '',
    '## How to cite a requirement',
    '',
    'Use the requirement identifier, for example [`ONDTF-GOV-001`](#ondtf-gov-001). Published ONDTF pages automatically link '
    '`ONDTF-*` identifiers to the corresponding entry in this register.',
    '',
    '## Register summary',
    '',
    '| Domain | Requirements |',
    '|---|---:|',
]
for domain, items in by_domain.items():
    lines.append(f'| {domain.replace("_", " ").title()} | {len(items)} |')

for domain, items in by_domain.items():
    lines += ['', f'## {domain.replace("_", " ").title()}', '']
    for req in items:
        rid=req['id']; anchor=rid.lower(); force=req.get('force','')
        statement=' '.join(str(req.get('statement','')).split())
        applicability=', '.join(f'`{x}`' for x in req.get('applicability') or []) or '—'
        accountable=req.get('accountable_role') or '—'
        responsible=', '.join(req.get('responsible_roles') or []) or '—'
        evidence=req.get('evidence') or []
        assertions_for=by_req.get(rid, [])
        caps=', '.join(req.get('capabilities') or []) or '—'
        lines += [
            f'<a id="{anchor}"></a>',
            f'### {rid}',
            '',
            f'**Normative force:** `{force}`  ',
            f'**Status:** `{req.get("status", "")}`  ',
            f'**Introduced:** `{req.get("introduced", "")}`',
            '',
            f'> **{force.replace("_", " ")}** — {statement}',
            '',
            '| Field | Governed value |',
            '|---|---|',
            f'| Applicability | {applicability} |',
            f'| Assessed object | {req.get("assessed_object") or "—"} |',
            f'| Accountable role | {accountable} |',
            f'| Responsible role(s) | {responsible} |',
            f'| Capability mapping | {caps} |',
            f'| Candidate assertion(s) | {", ".join(assertions_for) if assertions_for else "Not mapped"} |',
            '',
            '**Expected evidence**',
            '',
        ]
        if evidence:
            lines += [f'- {item}' for item in evidence]
        else:
            lines += ['- No evidence item recorded.']
        lines += ['', '[Back to register summary](#register-summary)', '']

OUT.write_text('\n'.join(lines).rstrip()+'\n', encoding='utf-8')
print(f'Requirements Register built: {len(reqs)} requirements across {len(by_domain)} domains')
