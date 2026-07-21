---
layout: default
title: Concept Dependency Map
parent: Documentation Architecture
nav_order: 3
---
# Concept Dependency Map

The central ONDTF concepts build on one another. Identity alone does not establish authority; technically valid evidence alone does not establish legitimacy; a decision is incomplete without attributable effect, review, and remedy.

```mermaid
flowchart LR
  ACT[Actor and participant] --> ID[Identity and role]
  ID --> AUTH[Authority]
  AUTH --> DEL[Delegation]
  DEL --> CRED[Credential and evidence]
  CRED --> POL[Policy and duties]
  POL --> ASS[Assurance]
  ASS --> DEC[Decision]
  DEC --> EFF[Effect]
  EFF --> REC[Receipt and audit]
  REC --> CH[Challenge]
  CH --> REM[Remedy]
  REM --> GOV[Governance learning]
  GOV --> POL
```

## Dependency matrix

| Topic | Depends on | Enables |
|---|---|---|
| Identity and role | Actor and context | Authority evaluation |
| Authority | Identity, competent source, scope | Delegation and admissible action |
| Delegation | Authority, scope, lifecycle | Bounded acting on behalf |
| Evidence | Issuer authority, provenance, status | Policy evaluation |
| Policy and duties | Governance authority, context | Decision constraints |
| Assurance | Evidence, controls, assessment | Reliance decisions |
| Decision | Policy, evidence, assurance | Effect and receipt |
| Effect | Authorised decision, execution boundary | Accountability |
| Challenge and remedy | Receipt, audit, affected party | Governance learning and correction |
