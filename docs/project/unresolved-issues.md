---
layout: default
title: Unresolved Issues Register
parent: Project Governance and Releases
nav_order: 9
---

# Unresolved issues register

## Purpose

This page records the maturity questions that remain after v0.6.0. Closure requires the evidence named in the canonical [`maturation-register.yaml`](../../model/project/maturation-register.yaml), not merely additional prose. The release has closed the architectural and operating-model items that were targeted for v0.6.0; implementation, pilot, interoperability and independent-review evidence remains intentionally open.

## Active issues

| ID | Issue | Risk | Target | Owner role | Status |
|---|---|---|---|---|---|
| URI-01 | No multi-implementation interoperability evidence | High | v0.8.0 | Implementation and Interoperability Workstream | Open |
| URI-02 | Quantitative thresholds require empirical calibration | Medium | v0.8.0 | Assurance and Evidence Workstream | Open |
| URI-03 | Jurisdiction profiles require competent current legal review | High | v0.7.0 | Jurisdiction Profile Maintainer | Open |
| URI-04 | Reference catalogues are not a complete conformance suite | High | v0.7.0 | Conformance Workstream | Open |
| URI-05 | Privacy-preserving status and cross-domain resolution patterns need comparison | Medium | v0.7.0 | Privacy Engineering Workstream | Open |
| URI-06 | Accessibility is not validated across downstream implementation patterns | High | v0.7.0 | Rights and Inclusion Workstream | Evidence Available |
| URI-13 | Performance, scale and recovery requirements lack tested baselines | Medium | v0.8.0 | Operations and Resilience Workstream | Open |
| URI-14 | Adversarial exercises and incident simulations have not been executed | High | v0.7.0 | Security and Resilience Workstream | Open |
| URI-15 | Internationalisation and terminology require cross-jurisdiction validation | Medium | v0.9.0 | Specification Editorial Workstream | Open |
| URI-16 | No assurance-equivalence model for cross-framework recognition | High | v0.8.0 | Recognition and Interoperability Workstream | Open |
| URI-17 | No end-to-end pilot of challenge, appeal and remedy | High | v0.7.0 | Rights and Redress Workstream | Evidence Available |

## Issues closed in v0.6.0

| ID | Resolution | Principal evidence |
|---|---|---|
| URI-07 | Standards and regulatory instruments may change after publication | `docs/project/reference-maintenance-policy.md`, `docs/project/standards-change-impact.md`, `model/project/controlled-document-register.yaml` |
| URI-08 | Role-specific normative obligations catalogue requires release review | `model/normative/requirement-catalogue.yaml`, `model/normative/requirement-schema.json`, `docs/normative/requirements-traceability.md` |
| URI-09 | No fully specified accreditation and certification operating model | `docs/conformance/index.md`, `model/conformance/assessment-scheme.yaml`, `model/conformance/conformance-claim.schema.json` |
| URI-10 | No complete provider lifecycle | `docs/operations/provider-lifecycle.md`, `model/operations/provider-lifecycle.yaml` |
| URI-11 | Institutional-governance operating model requires profile validation | `docs/governance/institutional-operating-model.md`, `model/governance/institutional-role-catalogue.yaml`, `model/governance/responsibility-assignment.yaml` |
| URI-12 | No complete sector-profile construction and validation method | `profiles/profile-methodology.md`, `profiles/profile-template.md`, `profiles/profile-validation.md` |
| URI-18 | No complete maintenance model for standards, profiles and controlled documents | `docs/project/controlled-document-governance.md`, `docs/project/profile-maintenance-policy.md`, `docs/project/reference-maintenance-policy.md` |
| URI-19 | No formal process for importing proven external-framework patterns | `docs/project/external-framework-pattern-adoption.md`, `model/project/maturation-register.yaml`, `model/profiles/external-adoption-register.yaml` |

## Release interpretation

The remaining high-risk issues do not invalidate the **Operational Framework Draft** claim because that claim concerns a complete and internally integrated operating architecture. They do prevent ONDTF from claiming independently demonstrated interoperability, production conformance, universal accessibility, empirically calibrated thresholds or proven cross-border recognition.

URI-06 and URI-17 now have operating-model evidence and remain open specifically for pilot validation. URI-04 remains open because a conformance architecture is not the same thing as an executable conformance suite. URI-03 remains open because a fictional worked profile cannot substitute for competent legal review of a real jurisdiction.

## Governance

An issue may remain open at release only where its impact is disclosed and does not contradict the release label. Issues affecting safety, internal consistency, publication integrity or truthful conformance claims must block release unless covered by an explicit, time-bounded risk-acceptance record.

See [Maturation Governance](maturation-governance.md), [Known Limitations](known-limitations.md), [Future Work](future-work.md) and [Implementation Evidence Programme](implementation-evidence.md).
