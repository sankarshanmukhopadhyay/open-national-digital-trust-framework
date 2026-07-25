---
title: Terminology Governance
parent: Controlled Vocabulary
nav_order: 1
---
# Terminology Governance

## Authority and scope

ONDTF independently governs the vocabulary used by its specification, profiles, conformance materials, machine-readable models, and release evidence. An external definition has no normative effect merely because it is mapped or cited.

## Decision rights

| Function | Accountable role | Evidence |
|---|---|---|
| Propose a term | Any contributor | Pull request and structured record |
| Editorial review | Specification Editorial Workstream | Review record |
| Domain review | Relevant workstream | Domain approval |
| Normative approval | ONDTF governance authority | Decision or approved pull request |
| Publication | Repository maintainers | Generated artefacts and CI logs |
| Deprecation or retirement | ONDTF governance authority | Replacement and migration record |

## Lifecycle

Terms move through `proposed`, `active`, `deprecated`, and `retired` states. Deprecation does not erase history. It must preserve the previous identifier, identify any replacement, and state the migration impact.

## Change classification

A clarification that does not alter conformance meaning may be commit-only. A backward-compatible new normative term normally requires a minor release. A changed definition that invalidates existing conforming interpretations requires explicit migration guidance and release-governance review.

## Assurance

CI validates structure, identifiers, aliases, references, source metadata, mappings, generated-output drift, and publication links. Semantic equivalence and jurisdictional neutrality remain accountable human review decisions.
