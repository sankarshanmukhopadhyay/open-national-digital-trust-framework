---
layout: default
title: Assessor Guide
parent: Implementation
nav_order: 4
---
# Assessor guide

**Status:** informative guidance.

ONDTF distinguishes machine-executable, assessor-verifiable and judgement-dependent assertions. An assessor must record the assessed object, applicable profile and version, evidence inspected, assertion outcome, competence basis, limitations and any skipped or not-applicable tests. A repository validation result is not a provider or scheme conformance claim.

```mermaid
flowchart TD
  SC[Determine scope and conformance class] --> AP[Resolve applicable requirements]
  AP --> EV[Collect evidence]
  EV --> EX{Assertion class?}
  EX -->|Machine-executable| T[Run test]
  EX -->|Assessor-verifiable| V[Inspect controlled evidence]
  EX -->|Judgement-dependent| J[Record structured judgement and rationale]
  T --> RR[Result record]
  V --> RR
  J --> RR
  RR --> DC[Scoped decision or finding]
```
