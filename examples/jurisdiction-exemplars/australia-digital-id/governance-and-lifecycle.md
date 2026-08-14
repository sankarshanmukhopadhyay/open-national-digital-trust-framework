---
layout: default
title: Governance and Lifecycle
parent: Australia Digital ID
nav_order: 1
---
# Australia Digital ID: governance and lifecycle

## Plain-language summary

This page turns the source-backed institutional arrangement into an ONDTF governance view. Modelled lifecycle states are analytical aids, not claims that the external framework uses the same labels.

## Governance flow

```mermaid
flowchart LR
  N0[Provider Accreditation]
  N1[Agdis Participation]
  N2[Relying Party Use]
  N3[Material Change]
  N4[Incident And Regulatory Response]
  N5[Suspension And Register Propagation]
  N0 --> N1
  N1 --> N2
  N2 --> N3
  N3 --> N4
  N4 --> N5
```

## Analytical state model

```mermaid
flowchart LR
  S0[prospective provider]
  S1[accreditation application]
  S2[accredited]
  S3[agdis participation application]
  S4[agdis approved]
  S5[operating]
  S6[material change review]
  S7[suspended or restricted]
  S8[withdrawn or expired]
  S0 --> S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8
```

These are ONDTF analytical states assembled from accreditation, approval, change, compliance and register concepts. They are not asserted to be statutory state labels.

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
