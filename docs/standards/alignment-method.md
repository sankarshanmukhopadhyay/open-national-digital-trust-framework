---
layout: default
title: Standards Alignment Method
parent: Standards Profile
nav_order: 4
---

# Standards alignment method

An ONDTF mapping states how an ONDTF requirement or capability relates to an external provision. It is not a legal opinion, certification result or claim of full conformity.

## Mapping relations

- **supports**: ONDTF content helps implement the external outcome;
- **partially supports**: ONDTF covers part of the external outcome;
- **depends on profile**: coverage exists only when a named profile selects additional requirements;
- **related**: concepts overlap but are not equivalent;
- **not addressed**: the external outcome is outside the current ONDTF scope.

Every mapping SHOULD identify the ONDTF source, external clause or outcome, relation, rationale, gaps, evidence expectations and reviewer date.

```mermaid
flowchart LR
  O[ONDTF requirement or capability] --> M[Mapping relation]
  E[External standard provision] --> M
  M --> R[Rationale and gap statement]
  R --> V[Reviewer and review date]
  V --> U[Update trigger]
```

Mappings MUST be reviewed when either source changes materially.
