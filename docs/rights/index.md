---
layout: default
title: Rights and Redress
parent: Open National Digital Trust Framework
nav_order: 17
has_children: true
---


# Rights and redress

ONDTF treats affected parties as governance subjects, not merely data subjects or transaction participants. A person or organisation may be affected by a trust decision without issuing, holding, presenting, or verifying a credential.

```mermaid
flowchart LR
  N[Notice or discovery] --> A[Access relevant record]
  A --> C[Challenge]
  C --> H[Independent handling]
  H --> D[Decision and explanation]
  D --> E{Escalation needed?}
  E -->|Yes| P[Appeal]
  E -->|No| R[Remedy and closure]
  P --> R
```

## Publication set

- [Affected Parties and Participation](affected-parties.md)
- [Transparency, Notice and Explanation](transparency-explanation.md)
- [Challenge, Grievance and Appeal](challenge-appeal.md)
- [Remedies and Accountability](remedies-accountability.md)
