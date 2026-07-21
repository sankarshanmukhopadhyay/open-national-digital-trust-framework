---
layout: default
title: Incident Response
parent: Canonical Workflows
nav_order: 7
---

# Incident response

```mermaid
flowchart LR
  D[Detect] --> T[Triage]
  T --> C[Contain]
  C --> P[Preserve evidence]
  P --> N[Notify]
  N --> R[Recover]
  R --> L[Learn and remediate]
```

Incident handling must preserve accountability while limiting further harm. The incident authority should coordinate technical containment, status changes, affected-party notice, cross-domain notification and evidence preservation.

A severity model SHOULD consider scale, sensitivity, authority compromise, persistence, irreversibility, vulnerable populations, cross-border reach and redress difficulty.
