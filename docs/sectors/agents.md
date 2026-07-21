---
title: AI and Software Agents
parent: Sector Profiles
nav_order: 5
---

# AI and Software-Agent Profile

Software agents are not treated as independent legal persons by default. They act through authority derived from a person or organisation and within an identifiable governance regime.

An agent action SHOULD be accompanied by evidence of:

- agent instance and software provenance;
- operator and accountable principal;
- delegated mandate;
- permitted tools and resources;
- policy and risk constraints;
- transaction context;
- human-oversight requirements;
- revocation and termination state.

```mermaid
sequenceDiagram
  participant U as Human or Organisation
  participant A as Agent
  participant T as Tool or Service
  participant R as Authority Resolver
  participant L as Evidence Log
  U->>A: Delegated mandate
  A->>T: Action request + mandate proof
  T->>R: Validate agent and authority
  R-->>T: Scope and status
  T-->>A: Execute or deny
  T->>L: Record action evidence
```
