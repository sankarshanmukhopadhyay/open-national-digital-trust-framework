---
layout: default
title: Information Governance
parent: Information Architecture
nav_order: 6
---

# Information governance

Information governance allocates responsibility for classification, quality, access, retention, correction and disposal.

| Information class | Examples | Default treatment |
|---|---|---|
| Public governance | policies, authority lists, conformance declarations | publish with provenance and versioning |
| Controlled operational | participant records, incident details | role-based access and audit |
| Sensitive evidence | personal or commercially sensitive evidence | minimise, encrypt and purpose-bind |
| Restricted assurance | vulnerabilities, audit workpapers | limited disclosure and retention |
| Redress records | challenges, reasons and remedies | protect parties while preserving reviewability |

## Governance obligations

- The authoritative owner MUST be named.
- Quality and correction responsibilities MUST be allocated.
- Retention MUST be tied to purpose, legal duty and redress period.
- Access MUST be logged where disclosure creates material risk.
- Derived data MUST retain sufficient provenance to evaluate fitness.
- Disposal MUST include replicas, caches and exported evidence where feasible.

Profiles should define data-protection roles and legal bases rather than embedding one jurisdiction's legal terminology in the core.
