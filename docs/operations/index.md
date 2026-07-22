---
title: Operations
parent: Open National Digital Trust Framework
nav_order: 8
has_children: true
---

# National Trust Operations

The operational model supports national coordination while preserving sectoral autonomy.

## Core operational functions

- trust registry operations;
- participant onboarding and offboarding;
- key and certificate lifecycle management;
- status distribution and cache management;
- incident coordination;
- vulnerability disclosure;
- conformance testing;
- assurance surveillance;
- transparency reporting;
- dispute and appeal administration.

## Trust event pipeline

```mermaid
flowchart LR
  S[Source system] --> E[Signed trust event]
  E --> B[Event broker]
  B --> R[Registry update]
  B --> M[Monitoring]
  B --> A[Audit evidence]
  M --> I[Incident response]
  I --> R
  I --> N[Notifications]
```


## Operational assurance integration

Operational monitoring, incident handling and service continuity feed the [Continuous Assurance and Trust Observability](../assurance/continuous-assurance.md) and [Operational Resilience](../assurance/operational-resilience.md) processes.
