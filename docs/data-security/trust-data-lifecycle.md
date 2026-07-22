---
layout: default
title: Trust Data Lifecycle
parent: Data Security
nav_order: 3
grand_parent: Open National Digital Trust Framework
---


# Trust data lifecycle

A lifecycle record SHOULD identify source, purpose, authority to process, transformations, recipients, storage locations, retention, status, and destruction evidence.

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Collected: purpose and authority approved
  Collected --> Active: validation complete
  Active --> Shared: authorised disclosure
  Shared --> Active: continuing use
  Active --> Restricted: dispute, incident or legal hold
  Restricted --> Active: restriction removed
  Active --> Archived: retention basis remains
  Archived --> Destroyed: retention expires
  Restricted --> Destroyed: authorised resolution
  Destroyed --> [*]
```

Systems SHALL prevent silent reuse for incompatible purposes. Material changes to purpose, recipient, sensitivity, or risk SHALL trigger reassessment and, where applicable, renewed notice, authorisation, or impact assessment.
