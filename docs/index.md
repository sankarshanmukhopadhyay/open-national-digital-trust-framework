---
layout: default
title: Open National Digital Trust Framework
nav_order: 1
has_children: true
permalink: /
---
# Open National Digital Trust Framework

ONDTF is an open, jurisdiction-neutral framework for designing digital trust infrastructure that can operate across sectors, technologies, institutions, and borders.

{: .highlight }
> **First visit?** Follow [ONDTF in One Hour](learning/one-hour.md) for the recommended introduction, or open [Learn ONDTF](learning/index.md) to choose a role-specific path.

<div class="ondtf-entry-grid">
  <a class="ondtf-entry-card" href="{{ '/docs/learning/executive-policy.html' | relative_url }}"><strong>Executive or policymaker</strong>Understand purpose, governance, risk, and adoption choices.</a>
  <a class="ondtf-entry-card" href="{{ '/docs/learning/architecture.html' | relative_url }}"><strong>Architect</strong>Study layers, components, boundaries, interactions, and information.</a>
  <a class="ondtf-entry-card" href="{{ '/docs/learning/governance.html' | relative_url }}"><strong>Governance designer</strong>Study authority, delegation, decision rights, accountability, and redress.</a>
  <a class="ondtf-entry-card" href="{{ '/docs/learning/security.html' | relative_url }}"><strong>Security or risk practitioner</strong>Trace assets, boundaries, adversaries, threats, controls, and evidence.</a>
  <a class="ondtf-entry-card" href="{{ '/docs/learning/implementation.html' | relative_url }}"><strong>Implementer</strong>Move from framework decisions to delivery and conformance.</a>
  <a class="ondtf-entry-card" href="{{ '/docs/learning/assurance.html' | relative_url }}"><strong>Assessor or auditor</strong>Study assurance, evidence, requirements, and conformance claims.</a>
</div>

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

## Two ways to use the documentation

| Mode | Use it when | Start here |
|---|---|---|
| Guided learning | You want a thorough understanding in a deliberate sequence | [Learn ONDTF](learning/index.md) |
| Reference lookup | You already know the domain or concept you need | Documentation map below |

## Documentation map

| Area | Purpose |
|---|---|
| [Core specification](core-specification/index.md) | Scope, concepts, capabilities, requirements, and conformance |
| [Target operating model](operating-model/index.md) | Institutional functions, lifecycles, decision rights, and maturity |
| [Foundations](foundations/index.md) | Scope, principles, terminology, and framework independence |
| [Reference architecture](architecture/index.md) | Responsibilities, services, layers, boundaries, and interactions |
| [Information architecture](information-model/index.md) | Canonical entities, relationships, lifecycle, identifiers, and provenance |
| [Governance](governance/index.md) | Authorities, communities, delegation, decisions, oversight, and redress |
| [Canonical workflows](workflows/index.md) | End-to-end lifecycle and trust-resolution flows |
| [Security](security/index.md) | Assets, assumptions, boundaries, adversaries, threats, and controls |
| [Data Security](data-security/index.md) | Data classification, lifecycle protection, provenance, retention, and breach response |
| [Privacy](privacy/index.md) | Purpose, minimisation, unlinkability, impact assessment, threats, and controls |
| [Rights and Redress](rights/index.md) | Affected parties, transparency, challenge, appeal, remedy, and accountability |
| [Assurance](assurance/index.md) | Assurance levels, evidence, assessment, and conformance |
| [Implementation](implementation/index.md) | Deployment patterns, implementation sequence, and reference interfaces |
| [Worked reference scenario](reference-scenario/index.md) | Instantiated artefacts and end-to-end traceability |
| [Jurisdiction profiles](../profiles/index.md) | National specialisation without weakening the core |
| [Documentation architecture](documentation/index.md) | Reading order, framework map, dependencies, and maintenance conventions |

## Current posture

ONDTF v0.5.0 is the Feature Complete Draft. It establishes the complete planned architectural baseline while remaining open to implementation evidence, interoperability testing, external review, and editorial refinement before candidate-specification status.
