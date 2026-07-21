---
title: Programme Management
nav_order: 20
has_children: true
---
# Programme Management

This section defines how ONDTF is developed as a controlled, multi-release standards programme. It provides the delivery discipline normally expected in a national-scale transformation: clear scope, accountable decisions, managed dependencies, measurable quality gates, and evidence-based release approvals.

## Programme outcomes

The programme will mature ONDTF from an initial seed into a candidate specification that is:

- semantically aligned with [TSMM](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model);
- operationally connected to [TIS](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas);
- jurisdiction-neutral at its core;
- profileable for countries and sectors;
- testable through conformance artefacts; and
- publishable in full through GitHub Pages.

## Delivery model

```mermaid
flowchart LR
  M0["M0 Mobilise"] --> M1["M1 Align semantics"]
  M1 --> M2["M2 Design operating model"]
  M1 --> M3["M3 Define architecture"]
  M2 --> M4["M4 Security, assurance and operations"]
  M3 --> M4
  M4 --> M5["M5 Jurisdiction and sector profiles"]
  M5 --> M6["M6 Implementation and conformance"]
  M6 --> M7["M7 Candidate review"]
```

See the [programme charter](charter.md), [integrated workplan](workplan.md), [quality gates](quality-gates.md), and [decision rights](decision-rights.md).
