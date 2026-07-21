---
title: Governance
parent: Open National Digital Trust Framework
nav_order: 3
has_children: true
---

# Governance Framework

National digital trust requires coordinated governance without collapsing all authority into one institution.

## Federated governance model

```mermaid
flowchart TB
  NTC[National Digital Trust Council] --> SA1[Sector Trust Authority]
  NTC --> SA2[State or Regional Trust Authority]
  NTC --> CB[Cross-border Coordination Function]
  SA1 --> TC1[Trust Community]
  SA1 --> TC2[Trust Community]
  SA2 --> TC3[Trust Community]
  TC1 --> P1[Issuers, Verifiers, Wallets, Registries]
  TC2 --> P2[Participants]
  TC3 --> P3[Participants]
  IA[Independent Assurance and Appeals] -.oversight.-> NTC
  IA -.oversight.-> SA1
  IA -.oversight.-> SA2
```

## National-level functions

A national coordination body SHOULD:

- maintain the core framework and national profiles;
- coordinate standards participation;
- operate or designate root discovery services where necessary;
- accredit or recognise assurance and conformance bodies;
- publish common risk, accessibility and privacy requirements;
- coordinate cross-sector and cross-border recognition;
- maintain national incident and vulnerability coordination;
- avoid becoming the universal transaction intermediary.

## Governance artefacts

Every recognised trust scheme MUST publish machine-readable and human-readable versions of:

- scope and purpose;
- participant roles;
- decision rights;
- membership and removal rules;
- credential and authority policies;
- assurance requirements;
- liability allocation;
- incident response;
- audit and transparency obligations;
- complaints, appeals and remedies;
- change management and versioning.
