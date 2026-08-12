---
layout: default
title: Reference Implementation Architecture
---
# Reference implementation architecture

The v0.7.0 reference implementation is an **informative executable view** of the normative models. Components deliberately map to governed responsibilities rather than technology products.

```mermaid
flowchart LR
  P[Profile and canonical models] --> L[Profile loader]
  L --> LC[Lifecycle controller]
  L --> PE[Policy evaluator]
  S[Status record] --> PE
  A[Authority evidence] --> PE
  PE --> R[Decision receipt]
  LC --> AU[Audit event stream]
  R --> AU
```

A successful software call is never treated as authority. Lifecycle transitions require the role and evidence declared by the canonical lifecycle model; authority evaluation remains distinct from identity or authentication.
