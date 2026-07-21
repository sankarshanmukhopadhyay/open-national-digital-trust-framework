---
title: Lifecycle and State
parent: Information Architecture
nav_order: 3
---
# Lifecycle and State

```mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Proposed
  Proposed --> Active: approved and published
  Proposed --> Rejected
  Active --> Suspended: temporary restriction
  Suspended --> Active: reinstated
  Active --> Superseded: replacement takes effect
  Active --> Revoked: authority withdrawn
  Active --> Expired: validity ends
  Superseded --> Archived
  Revoked --> Archived
  Expired --> Archived
  Rejected --> Archived
  Archived --> [*]
```

Lifecycle-sensitive decisions must evaluate status at a declared time and record the freshness of the status evidence. Historical evidence must remain interpretable after supersession or revocation without being mistaken for current authority.
