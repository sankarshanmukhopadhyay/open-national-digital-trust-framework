---
layout: default
title: Trust-scheme Lifecycle
parent: Target Operating Model
nav_order: 4
---

# Trust-scheme lifecycle

A trust scheme is a governed arrangement through which participants exchange or rely on evidence under common rules.

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Assessed
  Assessed --> Approved
  Approved --> Operational
  Operational --> Restricted
  Restricted --> Operational
  Operational --> Suspended
  Suspended --> Operational
  Suspended --> Retired
  Operational --> Retired
  Retired --> Archived
  Archived --> [*]
```

## Required lifecycle evidence

| Stage | Minimum evidence |
|---|---|
| Proposed | Purpose, affected parties, sponsor, scope, risk hypothesis |
| Assessed | Legal, security, privacy, assurance, interoperability, and sustainability assessment |
| Approved | Decision authority, effective date, profile, conditions, and review date |
| Operational | Participant register, service status, incidents, metrics, and changes |
| Restricted or suspended | Trigger, authority, scope, notification, continuity, and review |
| Retired | Exit plan, status preservation, data handling, outstanding obligations, and redress continuity |
| Archived | Retention basis, access controls, integrity, and disposal schedule |
