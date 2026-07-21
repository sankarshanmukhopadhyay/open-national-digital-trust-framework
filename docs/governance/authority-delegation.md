---
title: Authority and Delegation
parent: Governance
nav_order: 1
---

# Authority and Delegation

Identity establishes an actor. Authority establishes a permitted action.

A machine-verifiable authority statement SHOULD contain:

- principal;
- delegate;
- action or capability;
- object or resource;
- purpose;
- jurisdiction;
- valid-from and valid-until;
- transaction or value limits;
- delegation depth;
- conditions and obligations;
- revocation mechanism;
- evidence and audit requirements.

```mermaid
sequenceDiagram
  participant P as Principal
  participant D as Delegate or Agent
  participant V as Verifier
  participant R as Authority Registry
  P->>D: Issue bounded delegation credential
  D->>V: Request action + delegation proof
  V->>R: Resolve authority chain and status
  R-->>V: Valid, suspended, revoked or unknown
  V-->>D: Permit, deny or step-up
```

Delegation MUST NOT silently broaden through re-delegation. Each hop MUST preserve or narrow the original mandate unless the governing framework explicitly permits broader substitution.
