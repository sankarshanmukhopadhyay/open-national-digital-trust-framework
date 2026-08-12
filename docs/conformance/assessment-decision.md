---
layout: default
title: Assessment Decision
parent: Conformance and Accreditation
nav_order: 5
---

# Assessment decision

An assessment finding and a conformance decision are distinct. The assessment team evaluates evidence; the authorised decision function determines whether the claim may be issued, restricted, deferred or refused.

A decision MUST identify the assessed object, applicable profile and requirements, findings, unresolved exceptions, scope, conditions, validity, surveillance plan, reasons and appeal route. The decision maker MUST have access to sufficient evidence and MUST record conflicts and recusals.

## Assessment decision views

### Flow view
```mermaid
flowchart TD
  S[Assessment scope] --> E[Collect evidence]
  E --> A[Evaluate assertions]
  A --> N{Nonconformity?}
  N -->|no| D[Scoped conformance decision]
  N -->|yes| C[Corrective action]
  C --> R[Reassessment]
  R --> D
```

### State view
```mermaid
stateDiagram-v2
  [*] --> planned
  planned --> in_assessment
  in_assessment --> conformant
  in_assessment --> nonconformant
  nonconformant --> remediation
  remediation --> reassessment
  reassessment --> conformant
  reassessment --> nonconformant
```

### Swimlane view
```mermaid
sequenceDiagram
  participant Subject
  participant CAB as ROLE-CAB
  participant AA as ROLE-AA
  participant CAR as ROLE-CAR
  Subject->>CAB: Evidence package
  CAB->>CAB: Execute and verify assertions
  CAB-->>AA: Assessment record
  AA-->>Subject: Scoped decision or finding
  Subject->>CAR: Appeal where applicable
  CAR-->>Subject: Independent review outcome
```
