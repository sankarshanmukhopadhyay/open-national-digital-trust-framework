---
layout: default
title: Challenge and Correction
parent: Rights and Redress
nav_order: 12
---

# Challenge and correction

Challenge enables an affected party to contest evidence, identity binding, authority, delegation, status, policy interpretation or procedure. The process must support accessible intake, acknowledgement, preservation of records, correction of inaccurate data, interim protection where harm may continue and a reasoned outcome.

The framework must state which entity owns each correction action and how corrected information propagates to registries, relying parties, caches and downstream decisions.

## Challenge and correction views

### Flow view
```mermaid
flowchart TD
  N[Notice or discovered error] --> C[Challenge submitted]
  C --> E[Evidence made accessible]
  E --> D{Decision}
  D -->|uphold| X[Explain and expose appeal route]
  D -->|correct| U[Update authoritative record]
  U --> P[Propagate correction]
  P --> R[Record remedy and closure]
```

### State view
```mermaid
stateDiagram-v2
  [*] --> submitted
  submitted --> under_review
  under_review --> corrected
  under_review --> upheld
  upheld --> appealed
  appealed --> reversed
  appealed --> confirmed
  corrected --> closed
  reversed --> remedy_pending
  remedy_pending --> closed
```

### Swimlane view
```mermaid
sequenceDiagram
  participant AP as Affected Party
  participant SP as ROLE-SP
  participant CAR as ROLE-CAR
  participant RP as ROLE-RP
  AP->>CAR: Challenge evidence or decision
  CAR->>SP: Request authoritative evidence
  SP-->>CAR: Evidence + provenance
  CAR-->>AP: Review decision and explanation
  alt correction required
    CAR->>SP: Authorise correction
    SP->>RP: Propagate corrected state
    RP-->>CAR: Propagation receipt
  end
```
