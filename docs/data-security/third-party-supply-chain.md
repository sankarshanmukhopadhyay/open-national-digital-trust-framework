---
layout: default
title: Third-party and Supply-chain Data Governance
parent: Data Security
nav_order: 8
grand_parent: Open National Digital Trust Framework
---


# Third-party and supply-chain data governance

Delegating processing does not delegate accountability. Agreements and technical controls SHOULD define permitted purposes, locations, subprocessors, access, security measures, breach obligations, evidence rights, return or deletion, continuity, and termination.

```mermaid
flowchart LR
  O[Accountable organisation] --> P[Primary processor]
  P --> S[Subprocessor]
  O -. requirements and evidence .-> P
  P -. flowed-down obligations .-> S
  S -. telemetry and incident evidence .-> P
  P -. assurance evidence .-> O
```

Supply-chain controls SHOULD cover software provenance, build integrity, dependency risk, privileged support access, hosted key custody, data export, concentration risk, and exit capability.
