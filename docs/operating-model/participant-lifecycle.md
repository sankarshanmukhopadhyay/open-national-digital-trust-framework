---
layout: default
title: Participant Lifecycle
parent: Target Operating Model
nav_order: 5
---

# Participant lifecycle

Participant governance must continue after initial onboarding. Admission is not a permanent assurance conclusion.

```mermaid
stateDiagram-v2
  [*] --> Applicant
  Applicant --> Admitted
  Applicant --> Rejected
  Admitted --> Active
  Active --> Monitored
  Monitored --> Active
  Active --> Restricted
  Restricted --> Active
  Active --> Suspended
  Suspended --> Active
  Suspended --> Removed
  Active --> Exited
  Removed --> Archived
  Exited --> Archived
```

Admission criteria should address authority, competence, controls, conflicts, financial and operational resilience, evidence obligations, complaint handling, and exit readiness. Monitoring should be risk-based and capable of triggering step-up assessment, restriction, suspension, or removal.
