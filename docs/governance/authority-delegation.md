---
title: Authority and Delegation
parent: Governance
nav_order: 1
---

# Authority and Delegation

Identity establishes an actor. Authority establishes a permitted action.

A machine-verifiable authority statement SHOULD contain:

- principal;
- delegate;
- action or capability;
- object or resource;
- purpose;
- jurisdiction;
- valid-from and valid-until;
- transaction or value limits;
- delegation depth;
- conditions and obligations;
- revocation mechanism;
- evidence and audit requirements.

```mermaid
sequenceDiagram
  participant P as Principal
  participant D as Delegate or Agent
  participant V as Verifier
  participant R as Authority Registry
  P->>D: Issue bounded delegation credential
  D->>V: Request action + delegation proof
  V->>R: Resolve authority chain and status
  R-->>V: Valid, suspended, revoked or unknown
  V-->>D: Permit, deny or step-up
```

Delegation MUST NOT silently broaden through re-delegation. Each hop MUST preserve or narrow the original mandate unless the governing framework explicitly permits broader substitution.

## Authority evaluation views

### Flow view
```mermaid
flowchart TD
  I[Authenticated actor] --> A[Locate authority evidence]
  A --> S{Scope permits action?}
  S -->|no| D[Deny]
  S -->|yes| T{Time and conditions valid?}
  T -->|no| D
  T -->|yes| R{Revoked or suspended?}
  R -->|yes| D
  R -->|no| P[Permit or constrain]
  P --> RC[Decision receipt]
  D --> RC
```

### State view
```mermaid
stateDiagram-v2
  [*] --> proposed
  proposed --> active: authority established
  active --> suspended: temporary constraint
  suspended --> active: reinstated
  active --> revoked: revocation effective
  active --> expired: validity ends
  suspended --> revoked: revocation effective
```

### Swimlane view
```mermaid
sequenceDiagram
  participant Principal
  participant Delegate
  participant RP as ROLE-RP
  participant Status as Status service
  Principal->>Delegate: Bounded delegation
  Delegate->>RP: Request action + authority evidence
  RP->>Status: Check effective status and freshness
  Status-->>RP: Current status
  RP->>RP: Evaluate ONDTF-AUT-002 and ONDTF-AUT-003
  RP-->>Delegate: Permit deny or constrain + receipt
```
