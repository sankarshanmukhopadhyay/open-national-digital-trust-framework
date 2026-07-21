---
layout: default
title: Core Specification
nav_order: 4
has_children: true
---

# ONDTF Core Specification

The core specification defines the minimum outcomes, capabilities, responsibilities, and safeguards expected of a national digital trust framework. It is jurisdiction-neutral and does not require a particular meta-model, schema suite, protocol, registry product, or software stack.

## Normative posture

The core uses the terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** as described in the [normative language appendix](../appendices/normative-language.md). A jurisdiction or sector profile may strengthen a requirement but must not silently weaken it.

## Structure

| Section | Purpose |
|---|---|
| [Scope and non-goals](scope-and-non-goals.md) | Establishes the framework boundary |
| [Conceptual baseline](conceptual-baseline.md) | Defines the minimum shared concepts |
| [Capability model](capability-model.md) | Describes outcome-oriented capabilities |
| [Normative requirements](normative-requirements.md) | Establishes the core requirement set |
| [Conformance model](conformance-model.md) | Defines how claims are scoped and evidenced |
| [Traceability](traceability.md) | Links outcomes, capabilities, requirements, and evidence |

```mermaid
flowchart LR
  O[Public-interest outcomes] --> C[Required capabilities]
  C --> R[Normative requirements]
  R --> P[Jurisdiction and sector profiles]
  P --> I[Implementations]
  I --> E[Conformance evidence]
  E --> O
```
