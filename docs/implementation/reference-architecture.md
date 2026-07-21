---
title: Reference Deployment
parent: Implementation Guide
nav_order: 2
---

# Reference Deployment

```mermaid
flowchart TB
  subgraph Actors
    W[Wallet or Agent]
    I[Issuer]
    V[Verifier]
  end
  subgraph SharedServices[Shared trust services]
    TR[Trust Registry Federation]
    ST[Status Service]
    PS[Policy Service]
    EV[Evidence and Transparency]
  end
  subgraph Oversight
    GA[Governance Authority]
    AS[Assurance Body]
    RD[Redress Function]
  end
  I --> W
  W --> V
  V --> TR
  V --> ST
  V --> PS
  V --> EV
  GA --> TR
  AS -.assessment.-> I
  AS -.assessment.-> V
  RD --> EV
```

This topology is illustrative. Shared services may be operated by public, sectoral, cooperative or accredited private entities. Critical services SHOULD avoid single-provider concentration.
