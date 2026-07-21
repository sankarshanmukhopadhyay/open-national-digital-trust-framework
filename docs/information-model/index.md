---
layout: default
title: Information Architecture
parent: Open National Digital Trust Framework
nav_order: 3
has_children: true
---

# ONDTF Information Architecture

The information architecture defines the minimum semantics needed to govern and interoperate across trust domains. It is deliberately independent of a particular schema language or data model. Profiles may bind these concepts to JSON, XML, RDF, relational models or other representations.

```mermaid
classDiagram
  Jurisdiction "1" --> "0..*" TrustScheme
  TrustScheme "1" --> "1..*" GovernanceAuthority
  TrustScheme "1" --> "0..*" Participant
  GovernanceAuthority "1" --> "0..*" AuthorityGrant
  AuthorityGrant "1" --> "0..*" Delegation
  Participant "1" --> "0..*" Evidence
  Policy "1" --> "0..*" TrustDecision
  Evidence "0..*" --> "0..*" TrustDecision
  TrustDecision "1" --> "0..1" AdmittedEffect
  TrustDecision "1" --> "1" DecisionReceipt
  TrustDecision "0..1" --> "0..*" Challenge
  Challenge "0..1" --> "0..*" Remedy
```

## Publication set

- [Canonical entity catalogue](canonical-entities.md)
- [Relationships and cardinalities](relationships.md)
- [Lifecycle and state models](state-models.md)
- [Identifiers and references](identifiers.md)
- [Provenance and integrity](provenance.md)
- [Information governance](information-governance.md)
