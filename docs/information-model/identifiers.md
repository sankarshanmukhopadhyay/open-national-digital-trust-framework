---
layout: default
title: Identifiers and References
parent: Information Architecture
nav_order: 4
---

# Identifiers and references

ONDTF does not mandate a universal identifier scheme. It requires identifiers to be resolvable within their declared authority domain and unambiguous in the interaction context.

## Identifier requirements

An identifier MUST disclose or permit determination of:

- identifier type or namespace;
- issuing or controlling authority;
- subject or object class;
- uniqueness scope;
- lifecycle and reassignment policy;
- resolution mechanism where applicable;
- version or temporal reference where needed.

## Reference integrity

A reference to policy, evidence, status or a decision SHOULD be content-bound or version-bound where silent modification would affect interpretation. Human-readable labels MUST NOT be used as the sole authoritative reference.

## Correlation control

Profiles SHOULD avoid persistent cross-context identifiers unless necessary and proportionate. Pairwise, sector-specific, transaction-specific or purpose-bound identifiers may be used to reduce correlation.
