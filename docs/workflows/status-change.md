---
layout: default
title: Status Change and Suspension
parent: Canonical Workflows
nav_order: 5
---

# Status change and suspension

A status change is an authoritative lifecycle event, not merely a database update.

```mermaid
sequenceDiagram
  participant A as Authorised Authority
  participant S as Status Service
  participant N as Notification Service
  participant R as Relying Systems
  A->>S: Signed status event and effective time
  S->>S: Validate authority and prior state
  S->>N: Publish change notification
  N-->>R: Status update or invalidation signal
  R->>S: Resolve current state
  S-->>R: State, reason class and freshness
```

Emergency suspension MAY precede a full investigation where continued operation creates material risk. It must be time-bounded, reviewable and followed by notice and appeal appropriate to the context.
