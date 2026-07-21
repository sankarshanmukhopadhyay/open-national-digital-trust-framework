---
layout: default
title: Cross-domain Recognition
parent: Canonical Workflows
nav_order: 9
---

# Cross-domain recognition

```mermaid
sequenceDiagram
  participant A as Domain A
  participant G as Federation Gateway
  participant B as Domain B
  participant D as Local Decision Authority
  A->>G: Evidence and originating context
  G->>B: Resolve authority, status and assurance
  B-->>G: Authoritative response
  G->>G: Apply semantic and assurance mappings
  G->>D: Recognition package and limitations
  D-->>A: Local admit, condition, defer or deny
```

Recognition remains a local governance decision. A federation gateway must not silently convert foreign labels into local equivalence. The resulting decision must record mappings, limitations, current recognition status and redress responsibility.
