---
layout: default
title: Recognition Profiles and Equivalence
parent: Interoperability and Recognition
nav_order: 3
---
# Recognition profiles and equivalence

`REC-001` demonstrates bounded recognition. Equivalence is dimension-by-dimension (`EQV-001` through `EQV-004`), so an adoption can recognise attribution semantics while withholding equivalence for supervision or remedy.

```mermaid
flowchart TD
  R[Recognition request] --> A[Authority and legal/policy basis]
  A --> E[Dimension-by-dimension equivalence]
  E --> S[Scope and exclusions]
  S --> M[Monitoring and incident obligations]
  M --> D{Decision}
  D -->|recognise| L[Recognition lifecycle]
  D -->|reject| X[Recorded reasons]
```
