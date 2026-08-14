---
layout: default
title: Governance and Lifecycle
parent: EUDI Wallet Ecosystem
nav_order: 1
---
# EUDI Wallet Ecosystem: governance and lifecycle

## Plain-language summary

This page turns the source-backed institutional arrangement into an ONDTF governance view. Modelled lifecycle states are analytical aids, not claims that the external framework uses the same labels.

## Governance flow

```mermaid
flowchart LR
  N0[Wallet Provisioning]
  N1[Pid Provisioning]
  N2[Attestation Issuance]
  N3[Relying Party Registration]
  N4[Cross Border Presentation]
  N5[Selective Disclosure And Consent]
  N0 --> N1
  N1 --> N2
  N2 --> N3
  N3 --> N4
  N4 --> N5
```

## Analytical state model

```mermaid
flowchart LR
  S0[wallet solution designated or provided]
  S1[wallet unit issued]
  S2[wallet active]
  S3[credential or pid provisioned]
  S4[relying party request]
  S5[user approval or refusal]
  S6[presentation and verification]
  S7[status change or revocation]
  S8[wallet suspension or revocation]
  S9[migration or replacement]
  S0 --> S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9
```

These states combine wallet, credential and transaction lifecycles for ONDTF analysis. They are not presented as the canonical ARF state machine.

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
