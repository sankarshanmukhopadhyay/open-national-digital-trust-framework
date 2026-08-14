---
layout: default
title: Governance and Lifecycle
parent: UK DVS Trust Framework
nav_order: 1
---
# UK DVS Trust Framework: governance and lifecycle

## Plain-language summary

This page turns the source-backed institutional arrangement into an ONDTF governance view. Modelled lifecycle states are analytical aids, not claims that the external framework uses the same labels.

## Governance flow

```mermaid
flowchart LR
  N0[Cab Readiness]
  N1[Service Certification]
  N2[Register Entry]
  N3[Scoped Reliance]
  N4[Information Gateway]
  N5[Surveillance And Uplift]
  N0 --> N1
  N1 --> N2
  N2 --> N3
  N3 --> N4
  N4 --> N5
```

## Analytical state model

```mermaid
flowchart LR
  S0[candidate service]
  S1[assessment planned]
  S2[under assessment]
  S3[certified]
  S4[registered]
  S5[operating]
  S6[surveillance or reassessment]
  S7[certificate expiring]
  S8[suspended or ceased]
  S9[removed from register]
  S0 --> S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9
```

These are ONDTF analytical states derived from certification, register, surveillance/evaluation and expiry concepts; they are not a claim that the DVS framework uses this exact state vocabulary.

## Responsibility swimlane

```mermaid
sequenceDiagram
  participant Authority as Governance / supervisory authority
  participant Operator as Provider / platform operator
  participant Relying as Relying service
  participant Person as Individual / affected party
  Authority->>Operator: establish / verify applicable authority and status
  Operator->>Relying: provide service or evidence within scope
  Relying->>Operator: request current evidence / status
  Relying->>Person: explain request or consequential use
  Person->>Relying: approve, refuse or challenge where applicable
  Relying->>Authority: escalate material nonconformity / incident where required
  Authority->>Operator: review, constrain, suspend or require remediation
```

## ONDTF controls exercised

- `ONDTF-GOV-001` — authority basis must be explicit.
- `ONDTF-GOV-002` — governance, administration, supervision, assessment and remedy functions must be assigned.
- `ONDTF-AUT-002` — authority is evaluated for scope, purpose, time, conditions and revocation/status.
- `ONDTF-EVI-003` — registry/status information must expose authority, effective time and provenance.
- `ONDTF-INC-001` — material incidents require assigned detection, containment, evidence and coordination responsibilities.
- `ONDTF-MNT-002` — material external changes trigger impact review rather than silently changing ONDTF.

[Next: Assurance, Rights and Conformance](assurance-rights-and-conformance.md)
