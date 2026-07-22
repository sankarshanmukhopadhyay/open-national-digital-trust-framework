---
layout: default
title: Breach Response
parent: Data Security
nav_order: 7
grand_parent: Open National Digital Trust Framework
---


# Data breach response

A breach response SHALL consider confidentiality loss, integrity compromise, availability disruption, unauthorised correlation, provenance failure, and manipulation of trust decisions.

```mermaid
flowchart LR
  D[Detect] --> T[Triage]
  T --> C[Contain]
  C --> I[Investigate scope and trust impact]
  I --> N[Notify competent parties]
  N --> R[Recover and revalidate]
  R --> M[Remediate and learn]
  M --> A[Assurance reassessment]
```

Response records SHOULD identify affected data and people, compromised authority or decisions, status changes required, containment, notifications, recovery evidence, residual risk, and remedies. Where corrupted data may have produced decisions, response includes identifying and reviewing downstream effects.
