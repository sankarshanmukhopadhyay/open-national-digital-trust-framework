---
layout: default
title: Provider Lifecycle
parent: Operations
nav_order: 10
---

# Provider lifecycle

ONDTF treats participation as a governed lifecycle rather than a one-time registration event. A provider remains eligible only while its authority, assessed scope, service status and operating evidence remain current.

## Lifecycle states

```mermaid
stateDiagram-v2
  [*] --> Prospective
  Prospective --> Applicant: application accepted
  Applicant --> Assessed: assessment completed
  Assessed --> Approved: positive decision
  Assessed --> Rejected: negative decision
  Approved --> Active: registration and activation
  Active --> Restricted: conditions imposed
  Restricted --> Active: conditions cleared
  Active --> Suspended: material risk or nonconformity
  Restricted --> Suspended: escalation
  Suspended --> Active: reinstatement
  Suspended --> Withdrawn: withdrawal decision
  Active --> Exiting: voluntary or directed exit
  Exiting --> Archived: continuity and retention complete
  Rejected --> [*]
  Withdrawn --> Archived
  Archived --> [*]
```

The machine-readable state model is maintained in `model/operations/provider-lifecycle.yaml`.

## Governing requirements

A scheme profile MUST identify the authority responsible for admission, activation, restriction, suspension, reinstatement, withdrawal and exit. Each transition MUST have a recorded trigger, decision maker, evidence basis, effective time, notification duty and review route.

Provider approval MUST be scoped. It does not authorise services, jurisdictions, assurance levels or technical capabilities outside the assessed scope.

## Lifecycle controls

| Phase | Minimum controls | Primary evidence |
|---|---|---|
| Application | identity, authority, ownership, scope and conflict disclosures | application record |
| Due diligence | competence, financial, security, privacy and dependency review | due-diligence record |
| Assessment | requirement selection, evidence testing, findings and independence | assessment record |
| Approval | reasoned decision, conditions, validity and appeal route | approval decision |
| Activation | public status, service endpoints and effective time | register entry |
| Operation | monitoring, reporting, incident handling and change control | surveillance evidence |
| Restriction or suspension | proportionate control, notice, status propagation and review | status decision |
| Exit | continuity, participant migration, data disposition and archival | exit plan and closure record |

## Guided-construction hooks

The lifecycle model exposes decision points that the ONDTF Guided Framework Construction flow can ask adopters to resolve, including admission authority, evidence thresholds, validity periods, change triggers, suspension grounds, continuity obligations and appeal routes. These hooks are declared in `model/adoption/construction-input-contract.yaml` and do not themselves constitute the adaptive guided-construction flow.

## Three complementary views

The following views answer different implementation questions and remain subordinate to the canonical lifecycle model in `model/operations/provider-lifecycle.yaml`.

### Flow view — what happens?
```mermaid
flowchart TD
  P[Prospective] --> A[Application accepted]
  A --> AS[Assessment]
  AS --> D{Decision}
  D -->|positive| AP[Approved]
  D -->|negative| RJ[Rejected]
  AP --> AC[Active]
  AC -->|material risk| SU[Suspended]
  SU -->|criteria met| AC
  SU -->|withdrawal decision| WD[Withdrawn]
```

### State view — what states are valid?
```mermaid
stateDiagram-v2
  prospective --> applicant: PLT-001
  applicant --> assessed: PLT-002
  assessed --> approved: PLT-003
  assessed --> rejected: PLT-004
  approved --> active: PLT-005
  active --> restricted: PLT-006
  restricted --> active: PLT-007
  active --> suspended: PLT-008
  suspended --> active: PLT-009
  suspended --> withdrawn: PLT-010
  active --> exiting: PLT-011
  exiting --> archived: PLT-012
```

### Swimlane view — who acts?
```mermaid
sequenceDiagram
  participant P as Provider
  participant FA as ROLE-FA
  participant CAB as ROLE-CAB
  participant SA as ROLE-SA
  participant R as Registry
  P->>FA: Submit application
  FA->>CAB: Request assessment
  CAB-->>SA: Assessment evidence
  SA-->>FA: Approval or rejection decision
  FA->>R: Publish activation when conditions pass
  SA->>R: Publish restriction or suspension decision
  R-->>P: Effective status
```
