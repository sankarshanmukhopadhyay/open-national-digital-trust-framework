---
layout: default
title: Participant Onboarding
parent: Canonical Workflows
nav_order: 2
---

# Participant onboarding

```mermaid
flowchart TD
  A[Application] --> I[Identity and role validation]
  I --> U[Authority and eligibility checks]
  U --> R[Risk and assurance assessment]
  R --> D{Admission decision}
  D -->|Admit| P[Publish participant and role status]
  D -->|Condition| C[Record obligations and deadline]
  D -->|Deny| N[Notify reasons and challenge route]
  C --> P
```

Admission is role-specific. A participant admitted as an evidence provider is not automatically authorised as an assurance provider or scheme operator.

Required evidence includes application, identity and organisational standing, role eligibility, authority, control assessment, conflicts, accepted obligations, decision, effective date and status publication.
