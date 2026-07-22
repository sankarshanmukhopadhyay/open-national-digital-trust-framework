---
layout: default
title: Dependency and Adoption Governance
parent: Profiles
nav_order: 5
---
# Dependency and external-pattern adoption governance

External standards, legal instruments, institutional patterns, schemas, protocols, and services enter an ONDTF profile through explicit adoption records. A reference alone does not make an external dependency normative.

## Adoption lifecycle

```mermaid
flowchart LR
  I[Identify pattern or dependency] --> A[Abstract capability]
  A --> M[Map to ONDTF concepts]
  M --> D[Record adoption decision]
  D --> P[Pilot or evidence]
  P --> V[Approve for profile]
  V --> O[Operate and monitor]
  O --> R[Review, replace or retire]
```

Each adoption record must state:

- source and version;
- capability or pattern being adopted;
- ONDTF concepts and requirements affected;
- normative or informative status;
- profile scope;
- safeguards against semantic drift or lock-in;
- evidence and conformance implications;
- review owner and trigger;
- migration and retirement conditions.

The machine-readable register is `model/profiles/external-adoption-register.yaml`. The controlled dependency catalogue is `model/profiles/dependency-register.yaml`.

[Previous: Composition and Inheritance](profile-composition.md) · [Next: Versioning and Change](profile-versioning-and-change.md)
