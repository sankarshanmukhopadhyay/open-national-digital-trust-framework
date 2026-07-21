---
layout: default
title: Trust Resolution and Effect Admission
parent: Canonical Workflows
nav_order: 4
---

# Trust resolution and effect admission

```mermaid
flowchart TD
  P[Proposed effect] --> C[Establish interaction context]
  C --> I[Resolve participant and role]
  I --> A[Resolve authority and delegation]
  A --> O[Resolve applicable policy]
  O --> E[Validate evidence and status]
  E --> S[Evaluate assurance]
  S --> D{Decision}
  D -->|Admit| X[Execute bound effect]
  D -->|Condition| K[Require obligations]
  D -->|Defer| H[Human or external review]
  D -->|Deny| N[No effect]
  X --> R[Create receipt]
  K --> R
  H --> R
  N --> R
```

The decision receipt must identify the interaction context, authoritative sources, policy version, material evidence, outcome, conditions, accountable decision authority and challenge route. Sensitive evidence may be referenced rather than copied.
