---
title: Trust Lifecycle
parent: Architecture
nav_order: 3
---

# Trust Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Authorised: governance approval
  Authorised --> Active: onboarding and controls complete
  Active --> Suspended: incident or review
  Suspended --> Active: remediation accepted
  Active --> Revoked: authority withdrawn
  Active --> Expired: time limit reached
  Suspended --> Revoked
  Revoked --> Archived
  Expired --> Archived
  Archived --> [*]
```

The lifecycle applies to participants, credentials, delegated authorities, registry entries, policy versions and certification states.

Every lifecycle transition MUST identify the initiating authority, effective time, reason, evidence and notification obligations. High-impact transitions SHOULD support independent review and appeal.
