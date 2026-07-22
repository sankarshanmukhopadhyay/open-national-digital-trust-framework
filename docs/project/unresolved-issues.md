---
layout: default
title: Unresolved Issues Register
parent: Project Governance and Releases
nav_order: 9
---

# Unresolved issues register

## Purpose

Feature completeness does not require every design question to be closed. It requires remaining uncertainty to be explicit, bounded and governed. This page is the issue view of the canonical [`maturation-register.yaml`](../../model/project/maturation-register.yaml). Closure requires the specified evidence, not merely publication of additional prose.

| ID | Issue | Risk | Target | Owner role | Status |
|---|---|---|---|---|---|
| URI-01 | No multi-implementation interoperability evidence | High | v0.8.0 | Implementation and Interoperability Workstream | Open |
| URI-02 | Quantitative thresholds require empirical calibration | Medium | v0.8.0 | Assurance and Evidence Workstream | Open |
| URI-03 | Jurisdiction profiles require competent current legal review | High | v0.7.0 | Jurisdiction Profile Maintainer | Open |
| URI-04 | Reference catalogues are not a complete conformance suite | High | v0.7.0 | Conformance Workstream | Open |
| URI-05 | Privacy-preserving status and cross-domain resolution patterns need comparison | Medium | v0.7.0 | Privacy Engineering Workstream | Open |
| URI-06 | Accessibility is not validated across downstream implementation patterns | High | v0.7.0 | Rights and Inclusion Workstream | Open |
| URI-07 | Standards and regulatory instruments may change after publication | Medium | v0.6.0 | Reference Register Maintainer | Open |
| URI-08 | No complete role-specific normative obligations catalogue | High | v0.6.0 | Core Specification Workstream | Open |
| URI-09 | No fully specified accreditation and certification operating model | High | v0.6.0 | Conformance and Accreditation Workstream | Open |
| URI-10 | No complete provider lifecycle | High | v0.6.0 | Operating Model Workstream | Open |
| URI-11 | No operational institutional-governance profile for national deployment | High | v0.6.0 | Governance Workstream | Open |
| URI-12 | No complete sector-profile construction and validation method | Medium | v0.6.0 | Profile Architecture Workstream | Open |
| URI-13 | Performance, scale and recovery requirements lack tested baselines | Medium | v0.8.0 | Operations and Resilience Workstream | Open |
| URI-14 | Adversarial exercises and incident simulations have not been executed | High | v0.7.0 | Security and Resilience Workstream | Open |
| URI-15 | Internationalisation and terminology require cross-jurisdiction validation | Medium | v0.9.0 | Specification Editorial Workstream | Open |
| URI-16 | No assurance-equivalence model for cross-framework recognition | High | v0.8.0 | Recognition and Interoperability Workstream | Open |
| URI-17 | No end-to-end pilot of challenge, appeal and remedy | High | v0.7.0 | Rights and Redress Workstream | Open |
| URI-18 | No complete maintenance model for standards, profiles and controlled documents | Medium | v0.6.0 | Change Control Authority | Open |
| URI-19 | No formal process for importing proven external-framework patterns | Medium | v0.6.0 | Architecture and Profile Workstream | In progress |

## Required evidence by issue

Detailed closure evidence, linked programmes, candidate patterns and current dispositions are maintained in the machine-readable register. Examples include independent implementations for URI-01, pilot and incident evidence for URI-02, competent legal review for URI-03, executable positive and negative tests for URI-04, accessibility assessment for URI-06, and a controlled reference-maintenance procedure for URI-07 and URI-18.

## Governance

An issue may remain open at release only where its impact is disclosed and it does not invalidate the release claim. Issues affecting safety, internal consistency, publication integrity or truthful conformance claims must block release unless governed through an explicit exception and risk-acceptance record.

See [Maturation Governance](maturation-governance.md) for status and closure rules and [External Framework Pattern Adoption](external-framework-pattern-adoption.md) for the patterns being evaluated against these gaps.

## Available operational evidence

URI-09 and URI-10 now have draft evidence available. They remain open for worked-profile validation and release review rather than being treated as fully closed.
