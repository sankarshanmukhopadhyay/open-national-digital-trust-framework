---
layout: default
title: ONDTF in One Hour
parent: Learn ONDTF
nav_order: 1
---
# ONDTF in One Hour

**Audience:** anyone evaluating ONDTF for the first time  
**Prerequisites:** none  
**Estimated time:** 60 minutes  
**Outcome:** you should be able to explain what ONDTF governs, how its major parts fit together, and which deeper path to take next.

## Reading sequence

| Order | Read | Time | Question answered |
|---:|---|---:|---|
| 1 | [Framework overview](../index.md) | 8 min | What problem is ONDTF solving? |
| 2 | [Core principles](../foundations/principles.md) | 7 min | What design commitments constrain the framework? |
| 3 | [Conceptual baseline](../core-specification/conceptual-baseline.md) | 8 min | What are the essential trust concepts? |
| 4 | [Reference architecture](../architecture/index.md) | 8 min | How are responsibilities and system planes separated? |
| 5 | [Information architecture](../information-model/index.md) | 7 min | What information must be represented and traced? |
| 6 | [Governance framework](../governance/index.md) | 6 min | Who holds authority and how is it constrained? |
| 7 | [Security architecture](../security/index.md) | 7 min | What must be protected across the trust system? |
| 8 | [Worked reference scenario](../reference-scenario/index.md) | 7 min | Does the abstract framework close end to end? |
| 9 | [Implementation guide](../implementation/index.md) | 2 min | How does adoption begin? |

## Keep this mental model

```mermaid
flowchart LR
  I[Identity] --> A[Authority]
  A --> P[Policy and duties]
  P --> E[Evidence]
  E --> S[Assurance]
  S --> D[Decision]
  D --> F[Effect]
  F --> AC[Accountability]
  AC --> R[Redress]
```

ONDTF is not a credential format, registry product, identity system, or national platform. It is the governance and architecture framework that makes consequential digital interactions attributable, bounded, reviewable, and remediable.

## Choose your next path

- Decision-makers: [Executive and policy path](executive-policy.md)
- System designers: [Architecture path](architecture.md)
- Governance teams: [Governance path](governance.md)
- Security and risk teams: [Security path](security.md)
- Delivery teams: [Implementation path](implementation.md)
- Assessors: [Assurance and assessment path](assurance.md)
