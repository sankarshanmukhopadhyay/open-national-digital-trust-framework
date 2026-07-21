---
layout: default
title: Authority Grant and Delegation
parent: Canonical Workflows
nav_order: 3
---

# Authority grant and delegation

```mermaid
sequenceDiagram
  participant P as Principal Authority
  participant R as Authority Registry
  participant D as Delegate
  participant V as Relying Service
  P->>D: Grant bounded delegation
  D-->>P: Accept duties and constraints
  P->>R: Publish grant and status
  D->>V: Request action with delegation reference
  V->>R: Resolve chain and current status
  R-->>V: Scope, constraints and status
  V-->>D: Admit, condition or deny
```

A delegation MUST identify source authority, delegate, actions, subjects, purpose, jurisdiction, validity, onward-delegation rights and termination conditions. Every child delegation must be no broader than its parent.

A verifier MUST reject a chain with missing links, expired authority, prohibited onward delegation or incompatible purpose.
