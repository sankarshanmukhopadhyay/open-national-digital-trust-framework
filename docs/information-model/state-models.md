---
layout: default
title: Lifecycle and State Models
parent: Information Architecture
nav_order: 3
---

# Lifecycle and state models

State transitions are governance events. A transition MUST identify the authorised actor, effective time, reason and supporting evidence.

## Generic governed-entity lifecycle

```mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Approved: authorised approval
  Approved --> Active: effective date reached
  Active --> Suspended: risk or non-compliance
  Suspended --> Active: reinstatement
  Active --> Superseded: replacement becomes effective
  Active --> Revoked: authority withdrawn
  Suspended --> Revoked: final withdrawal
  Superseded --> Archived
  Revoked --> Archived
  Archived --> [*]
```

## Decision lifecycle

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Evaluating
  Evaluating --> Admitted
  Evaluating --> Denied
  Evaluating --> Deferred
  Evaluating --> Conditioned
  Conditioned --> Admitted: obligations satisfied
  Conditioned --> Denied: obligations failed
  Admitted --> Executed
  Admitted --> Expired
  Executed --> Challenged
  Denied --> Challenged
  Challenged --> Upheld
  Challenged --> Corrected
  Corrected --> Remedied
```

## Required transition metadata

- entity identifier and prior state;
- requested and resulting state;
- transition authority;
- policy and reason code;
- decision time and effective time;
- evidence references;
- notification and review requirements.

Profiles MAY define additional states but MUST preserve the meaning of core terminal and restriction states.
