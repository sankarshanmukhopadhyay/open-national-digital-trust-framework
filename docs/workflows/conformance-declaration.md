---
layout: default
title: Conformance Declaration
parent: Canonical Workflows
nav_order: 10
---

# Conformance declaration

A conformance declaration MUST be scoped to a named profile, version, capability set, deployment boundary and assessment basis.

```mermaid
flowchart TD
  S[Select profile and class] --> T[Execute tests and assessments]
  T --> E[Assemble evidence package]
  E --> D[Issue scoped declaration]
  D --> P[Publish status and limitations]
  P --> M[Monitor changes and expiry]
  M --> R[Renew, suspend or withdraw]
```

The declaration must identify exclusions, compensating controls, assessment date, evidence freshness, assessor relationship and expiry. Use of an aligned technology or schema does not itself establish ONDTF conformance.
