---
layout: default
title: Guided Construction Readiness
parent: Adoption
nav_order: 8
---

# Guided construction readiness

Commit 2 prepares the provider-lifecycle and conformance models for the planned **ONDTF Guided Framework Construction** capability in Commit 4. It does not yet implement the full adaptive question flow.

## Construction contract

`model/adoption/construction-input-contract.yaml` identifies decisions that a future guided flow must collect and maps them to generated fields, requirements, evidence and review gates. The contract currently covers:

- admission and activation authority;
- provider and service scope;
- validity and surveillance;
- material-change classification;
- restriction, suspension and withdrawal;
- continuity and exit;
- conformance claim type;
- assessment independence;
- assessor accreditation;
- evidence retention;
- appeals and public status.

## Design rule

The future generator must distinguish an adopter-supplied decision, an inherited ONDTF default, a profile-controlled choice, an unresolved decision and a matter requiring legal, technical or stakeholder review. It must not silently fill authority, liability or rights-sensitive decisions.

```mermaid
flowchart LR
  Q[Guided question] --> D[Recorded decision]
  D --> F[Model field]
  D --> R[Applicable requirement]
  D --> E[Evidence obligation]
  D --> G[Review gate]
  F --> O[Generated DTF artefacts]
  R --> O
  E --> O
  G --> O
```
