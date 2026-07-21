---
layout: default
title: Framework Map
parent: Documentation Architecture
nav_order: 2
---
# Framework Map

Use this map to regain orientation and move between the main bodies of ONDTF.

```mermaid
flowchart TB
  HOME[Framework overview] --> F[Foundations]
  F --> C[Core specification]
  C --> TOM[Target operating model]
  C --> RA[Reference architecture]
  TOM --> G[Governance]
  RA --> IM[Information architecture]
  G --> WF[Canonical workflows]
  IM --> WF
  WF --> SEC[Security architecture]
  SEC --> ASS[Assurance and conformance]
  ASS --> OPS[Operations and implementation]
  OPS --> RS[Worked reference scenario]
  RS --> PROF[Sector and jurisdiction profiles]

  click HOME "../index.html" "Framework overview"
  click F "../foundations/index.html" "Foundations"
  click C "../core-specification/index.html" "Core specification"
  click TOM "../operating-model/index.html" "Target operating model"
  click RA "../architecture/index.html" "Reference architecture"
  click G "../governance/index.html" "Governance"
  click IM "../information-model/index.html" "Information architecture"
  click WF "../workflows/index.html" "Canonical workflows"
  click SEC "../security/index.html" "Security architecture"
  click ASS "../assurance/index.html" "Assurance"
  click OPS "../implementation/index.html" "Implementation"
  click RS "../reference-scenario/index.html" "Worked scenario"
```

## Three ways through the framework

- **Learn:** follow a curated [learning path](../learning/index.md).
- **Look up:** use the sidebar and search.
- **Validate:** follow the [worked reference scenario](../reference-scenario/index.md) and its evidence package.
