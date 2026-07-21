---
layout: default
title: Challenge, Appeal and Remedy
parent: Canonical Workflows
nav_order: 8
---

# Challenge, appeal and remedy

```mermaid
stateDiagram-v2
  [*] --> Submitted
  Submitted --> Acknowledged
  Acknowledged --> UnderReview
  UnderReview --> Upheld
  UnderReview --> Corrected
  UnderReview --> Escalated
  Escalated --> AppealDecided
  Corrected --> RemedyOrdered
  AppealDecided --> RemedyOrdered
  RemedyOrdered --> RemedyVerified
  Upheld --> Closed
  RemedyVerified --> Closed
```

A challenge route must be discoverable, accessible and proportionate to impact. The reviewing authority needs access to sufficient evidence to understand the decision while protecting unrelated parties and sensitive security information.

Remedies may include correction, re-evaluation, restoration, suspension, notification, compensation, policy change or systemic remediation. Completion requires evidence, not merely an internal status update.
