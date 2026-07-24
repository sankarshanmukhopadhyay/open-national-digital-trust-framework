---
layout: default
title: Sectoral Standards Adoption Strategy
parent: Standards Profile
nav_order: 7
---

# Sectoral standards adoption strategy

ONDTF uses a sectoral standards layer to determine how external standards contribute to a specific operating context. The layer does not treat a reference, citation or thematic match as formal adoption.

## Operating principle

A sector profile must answer five distinct questions:

1. Which sector transactions, services, actors and affected parties are in scope?
2. Which capabilities and lifecycle functions are required?
3. Which external standards are relevant to those capabilities?
4. Which parts are adopted, excluded or supplemented, and under whose authority?
5. What evidence, review, migration and retirement controls govern continued reliance?

```mermaid
flowchart LR
  S[Sector outcomes and harms] --> C[Required capabilities]
  C --> R[Relevant standards]
  R --> D[Bounded adoption decision]
  D --> E[Evidence and conformance]
  E --> M[Monitoring migration and retirement]
```

## Canonical artefacts

- [`sector-taxonomy.yaml`]({{ '/model/references/sector-taxonomy.yaml' | relative_url }}) defines controlled sector identifiers.
- [`adoption-taxonomy.yaml`]({{ '/model/references/adoption-taxonomy.yaml' | relative_url }}) defines adoption states and modes.
- [`sector-standard-mapping.schema.json`]({{ '/model/references/sector-standard-mapping.schema.json' | relative_url }}) defines the mapping record.
- `model/references/sector-standard-mappings/` contains sector mapping instances.

The central standards register remains the authoritative catalogue of publications. Sector mappings reference its stable identifiers and must not duplicate or silently override publication metadata.

## Adoption states

| State | Meaning |
|---|---|
| Discovered | Potentially relevant and awaiting assessment. |
| Mapped | Capabilities, lifecycle relevance and gaps have been identified. |
| Candidate | Proposed for bounded adoption and awaiting authorised decision or pilot evidence. |
| Adopted | Formally approved for a named profile, scope and version. |
| Retired | No longer approved for new implementations; migration or historical traceability applies. |

## Adoption modes

| Mode | Effect |
|---|---|
| Informative reference | Context or comparison only. |
| Capability adoption | Selected outcomes or capabilities are reused without wholesale adoption. |
| Partial normative adoption | Identified clauses, profiles or requirements become normative within a named profile. |
| Normative profile dependency | A named external publication and version are required by the profile. |

## Required decision content

Every candidate or adopted mapping must identify:

- the canonical standard identifier and version;
- sector relevance and lifecycle functions;
- selected and excluded scope;
- adoption mode and disposition;
- rationale and known gaps;
- evidence and conformance implications;
- legal, institutional or profile conflicts;
- approving authority and review owner;
- review, supersession, migration and retirement triggers.

A technical standard must not be represented as satisfying governance, authority, rights, accessibility, remedy or legal-effect requirements that remain outside its scope.

## Phased adoption

### Phase 1: discovery

Define sector outcomes, transactions, authorities, affected parties, harms, applicable obligations and existing schemes. No standard becomes normative.

### Phase 2: capability and gap mapping

Assess candidate standards against ONDTF requirements, lifecycle stages, actor responsibilities, assurance, evidence, rights and interoperability. Record adequate, partial, conflicting, irrelevant and unresolved coverage.

### Phase 3: adoption proposition

Specify selected scope, exclusions, supplementary ONDTF controls, evidence, migration consequences and the authority competent to approve adoption.

### Phase 4: controlled pilot

Test ordinary and adverse journeys, including stale status, revoked authority, service outage, inaccessible channels, correction propagation and disputed outcomes.

### Phase 5: profile approval

Approve the selected standards, obligation level, conformance route, surveillance, remedy, migration period and emergency suspension controls.

### Phase 6: progressive deployment

Progress from exploratory and mapped states through pilot-approved, sector-recommended, sector-required and mature operation. A publication must not move directly from recognised relevance to mandatory dependency.

### Phase 7: continuous governance

Review new editions, vulnerabilities, regulation, implementation failures, complaints, interoperability defects, concentration risk and divergence between sector implementations.

## Initial sequencing

The initial illustrative mappings cover public services and financial services. Public services pressure-test statutory authority, essential-service access, exclusion, accessibility and remedy. Financial services pressure-test transaction assurance, fraud, auditability, delegation and high-frequency status decisions.

These mappings are architectural examples in v0.6.0. They are not approved sector profiles, legal determinations or regulator endorsements. v0.7.0 should convert them into reviewed pilot propositions; v0.8.0 should use them in cross-sector interoperability and recognition testing; v0.9.0 should establish candidate-level maintenance and retirement governance.
