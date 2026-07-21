---
layout: default
title: Governance Decision Records
parent: Governance
nav_order: 5
---
# Governance Decision Records

Material governance choices should produce an immutable, attributable decision record containing the decision, authority, affected scope, evidence considered, dissent or conflict declarations, effective date, review date, supersession conditions, and appeal route.

```mermaid
sequenceDiagram
  participant P as Proposer
  participant A as Competent authority
  participant R as Reviewers
  participant G as Governance registry
  participant I as Implementers
  P->>A: Submit proposal and impact assessment
  A->>R: Request review
  R-->>A: Findings, dissent, conditions
  A->>G: Publish signed decision record
  G-->>I: Current policy and effective date
  I->>G: Implementation evidence
```
