---
layout: default
title: Challenge, Grievance and Appeal
parent: Rights and Redress
nav_order: 3
grand_parent: Open National Digital Trust Framework
---


# Challenge, grievance and appeal

A challenge process SHALL accept disputes about identity, authority, evidence, status, policy application, procedural fairness, privacy, and resulting effects.

```mermaid
stateDiagram-v2
  [*] --> Submitted
  Submitted --> AdmissibilityReview
  AdmissibilityReview --> Investigation: accepted
  AdmissibilityReview --> Closed: out of scope with reasons
  Investigation --> InterimProtection: risk of continuing harm
  InterimProtection --> Determination
  Investigation --> Determination
  Determination --> Remedy
  Determination --> Appeal: eligible appeal
  Appeal --> Remedy
  Remedy --> Closed
```

Processes SHOULD specify deadlines, independence, evidence access, interim safeguards, conflict handling, escalation, and preservation of records.
