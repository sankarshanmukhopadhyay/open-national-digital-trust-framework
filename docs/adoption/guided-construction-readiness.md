---
layout: default
title: Construction Model Evolution
parent: Adoption
nav_order: 8
---
# Construction model evolution

The guided-construction model is built on stable decision contracts exposed by the normative, institutional, lifecycle, conformance, assurance, and rights models. Those contracts make it possible to add or refine questions without rewriting the underlying ONDTF domains.

The current implementation separates:

- domain decision inputs in `construction-input-contract.yaml`;
- user-facing staged questions in `question-catalogue.yaml`;
- reusable options in `pattern-catalogue.yaml`;
- consistency rules in `contradiction-rules.yaml`;
- completion criteria in `completeness-gates.yaml`.

This separation preserves traceability and allows future tooling to evolve without turning questionnaire wording into normative requirements.

[Previous: Model and Implementation Guide](guided-construction-model.md)
