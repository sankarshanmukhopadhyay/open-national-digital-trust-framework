---
layout: default
title: Cross-border Recognition
parent: Jurisdiction Profiles
nav_order: 4
---


# Cross-border recognition

Cross-border operation creates two separate questions:

1. whether an authority, credential, assurance result, or decision is recognised; and
2. whether data may lawfully and safely move, be accessed, or be processed across borders.

```mermaid
flowchart LR
  A[Origin jurisdiction] --> R[Recognition assessment]
  R --> E[Evidence and assurance equivalence]
  E --> D[Destination decision]
  A --> T[Data-transfer assessment]
  T --> D
  D --> C[Conditions, restrictions or refusal]
```

Profiles SHOULD document legal basis, transfer mechanism, location and access, onward transfer, oversight, redress, incident cooperation, evidence equivalence, revocation propagation, and exit arrangements.
