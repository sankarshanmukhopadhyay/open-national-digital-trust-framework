---
title: Information Model
nav_order: 5
has_children: true
---
# Information Model

The ONDTF information model provides a self-contained vocabulary for architecture, profiles, controls, and conformance. Optional crosswalks connect it to TSMM, TIS, and other compatible resources. It provides a stable vocabulary for architecture, profiles, controls, and conformance.

```mermaid
flowchart LR
  J["Jurisdiction"] --> S["Trust scheme"]
  S --> GA["Governance authority"]
  GA --> AG["Authority grant"]
  AG --> P["Participant"]
  P --> IC["Interaction context"]
  IC --> PO["Policy"]
  IC --> EV["Evidence"]
  PO --> TD["Trust decision"]
  EV --> TD
  TD --> EF["Admitted effect"]
  TD --> DR["Decision receipt"]
  EF --> CH["Challenge and remedy"]
```

See [entities](entities.md), [relationships](relationships.md), [lifecycle](lifecycle.md), and [identifier and provenance rules](identifiers-provenance.md).
