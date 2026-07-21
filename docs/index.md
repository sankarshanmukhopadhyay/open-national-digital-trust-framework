---
layout: default
title: Open National Digital Trust Framework
nav_order: 1
has_children: true
permalink: /
---

# Open National Digital Trust Framework

ONDTF is an open, jurisdiction-neutral framework for designing national digital trust infrastructure that can operate across sectors, technologies, institutions, and borders.

## Design objective

A consequential digital interaction should be capable of producing sufficient evidence that:

1. the actor was identifiable at the required level;
2. the actor held current and bounded authority;
3. applicable policy and duty constraints were evaluated;
4. the evidence and assurance were appropriate to the risk;
5. the resulting effect was attributable and reviewable; and
6. challenge, revocation, remediation, and redress remained available.

```mermaid
flowchart LR
  A[Actor or system] --> I[Identity and role]
  I --> AU[Authority]
  AU --> P[Policy and duties]
  P --> E[Evidence]
  E --> AS[Assurance]
  AS --> D[Decision]
  D --> F[Effect]
  F --> AC[Accountability]
  AC --> R[Redress]
```

## Documentation map

| Area | Purpose |
|---|---|
| [Core specification](core-specification/index.md) | Scope, concepts, capabilities, requirements, and conformance |
| [Target operating model](operating-model/index.md) | Institutional functions, lifecycles, decision rights, and maturity |
| [Programme management](programme/index.md) | Delivery governance, workplan, decisions, and quality gates |
| [Information model](information-model/index.md) | Canonical entities, relationships, lifecycle, identifiers, and provenance |
| [Foundations](foundations/index.md) | Scope, principles, terminology, TSMM/TIS relationship |
| [Architecture](architecture/index.md) | Trust model, actors, lifecycle, runtime interactions |
| [Governance](governance/index.md) | Authorities, communities, delegation, decisions, redress |
| [Standards](standards/index.md) | Interoperability and standards-selection rules |
| [Security](security/index.md) | Threat model, controls, recovery, and trust-boundary protection |
| [Assurance](assurance/index.md) | Assurance levels, evidence, assessment, and continuous assurance |
| [Operations](operations/index.md) | Operational services, events, metrics, and incident coordination |
| [Sector profiles](sectors/index.md) | Reusable sector profiling method and examples |
| [Jurisdiction profiles](../profiles/index.md) | National adoption profiles, beginning with India |
| [Implementation](implementation/index.md) | Deployment patterns, conformance, and reference interfaces |
| [International](international/index.md) | Federation and mutual-recognition patterns |
| [Adoption](adoption/index.md) | Reader paths and staged adoption |

## Release posture

Version 0.3.0 establishes the first coordinated core specification and national digital trust target operating model. It introduces an outcome-oriented capability model, a normative requirement baseline, scoped conformance, institutional functions, governance lifecycles, operational redress, and staged maturity. It remains a public draft and does not yet claim complete reference interfaces, sector profiles, or production certification.
