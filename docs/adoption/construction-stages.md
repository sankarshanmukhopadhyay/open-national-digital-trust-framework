---
layout: default
title: Construction Stages
parent: Adoption
nav_order: 2
---
# Construction stages

The guided flow is organised into eleven stages. Branching logic may skip non-applicable questions, but no stage may be silently omitted.

| Stage | Decision focus | Principal outputs |
|---:|---|---|
| 1 | purpose, scope, harms, exclusions | charter and scope |
| 2 | authority and legitimacy | authority basis and governance |
| 3 | roles and decision rights | role catalogue and responsibility matrix |
| 4 | participation and lifecycle | admission, operation, suspension, exit |
| 5 | assurance | dimensions, levels, evidence, failure outcomes |
| 6 | conformance and accreditation | claim types, assessment, surveillance |
| 7 | technology and registries | dependency and status model |
| 8 | rights, accessibility, remedy | affected-party operating model |
| 9 | risk and adversarial conditions | risk register and control priorities |
| 10 | recognition and interoperability | recognition profile |
| 11 | maintenance and evolution | controlled-document and migration model |

A stage can be marked complete only when required decisions are resolved or explicitly accepted as a governed open issue with an authorised owner and review date.

```mermaid
flowchart TD
  S1[Scope] --> S2[Authority]
  S2 --> S3[Roles]
  S3 --> S4[Lifecycle]
  S4 --> S5[Assurance]
  S5 --> S6[Conformance]
  S6 --> S7[Technology and registries]
  S7 --> S8[Rights and remedy]
  S8 --> S9[Risk]
  S9 --> S10[Recognition]
  S10 --> S11[Maintenance]
```

[Previous: Guided Framework Construction](guided-framework-construction.md) · [Next: Decision States and Review Gates](decision-states-and-review-gates.md)
