---
title: Relationships and Cardinality
parent: Information Model
nav_order: 2
---
# Relationships and Cardinality

```mermaid
classDiagram
  class Jurisdiction
  class TrustScheme
  class GovernanceAuthority
  class Participant
  class AuthorityGrant
  class Delegation
  class InteractionContext
  class Policy
  class Evidence
  class TrustDecision
  class DecisionReceipt
  class AdmittedEffect
  class Challenge
  class Remedy

  Jurisdiction "1" --> "0..*" TrustScheme : profiles
  TrustScheme "1" --> "1..*" GovernanceAuthority : governedBy
  TrustScheme "1" --> "0..*" Participant : admits
  GovernanceAuthority "1" --> "0..*" AuthorityGrant : issues
  AuthorityGrant "1" --> "0..*" Delegation : permits
  Participant "1..*" --> "0..*" InteractionContext : participatesIn
  InteractionContext "1" --> "1..*" Policy : governedBy
  InteractionContext "1" --> "0..*" Evidence : evaluates
  InteractionContext "1" --> "1" TrustDecision : produces
  TrustDecision "1" --> "1" DecisionReceipt : recordedBy
  TrustDecision "1" --> "0..1" AdmittedEffect : permits
  AdmittedEffect "0..1" --> "0..*" Challenge : contestedBy
  Challenge "1" --> "0..*" Remedy : resolvedBy
```

## Relationship rules

An admitted effect must be attributable to one trust decision. A trust decision must reference the applicable interaction context, policy basis, evaluating authority, and evidence set. Derived authority must preserve an unbroken lineage to a valid root authority. A challenge must remain linked to the challenged decision or effect even when the original artefact is superseded.
