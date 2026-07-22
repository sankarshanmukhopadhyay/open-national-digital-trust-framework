---
layout: default
title: Unresolved Issues Register
parent: Project Governance and Releases
nav_order: 9
---

# Unresolved issues register

## Purpose

Feature completeness does not require every design question to be closed. It requires remaining uncertainty to be explicit, bounded and governed. This register identifies matters that may affect adoption or the path to Candidate Specification status.

| ID | Issue | v0.5.0 disposition | Required next evidence |
|---|---|---|---|
| URI-01 | No multi-implementation interoperability evidence is yet available. | Accepted limitation for a feature-complete draft. | Independent profile implementations and cross-vendor test results. |
| URI-02 | Quantitative thresholds in risk, assurance and operational metrics require empirical calibration. | Published as profile-governed parameters, not universal constants. | Pilot data, incident evidence and sector review. |
| URI-03 | Jurisdiction profiles are informative and require current legal review before adoption. | Clearly labelled and separated from the jurisdiction-neutral core. | Competent legal and regulatory review in each adopting jurisdiction. |
| URI-04 | Machine-readable catalogues are reference artefacts rather than a complete conformance test suite. | Accepted for v0.5.0. | Executable assertions, negative tests and independent implementation evidence. |
| URI-05 | Privacy-preserving status, registry and cross-domain resolution patterns require implementation comparison. | Architectural requirements are present; mechanisms remain profile-dependent. | Comparative implementation and privacy analysis. |
| URI-06 | Accessibility has been addressed at documentation level but not validated across every downstream implementation pattern. | Documentation checks retained; implementation obligation remains explicit. | Accessibility review of pilot user journeys and interfaces. |
| URI-07 | Standards and regulatory instruments may change after publication. | Central register includes status and review metadata. | Release-time review and monitored maintenance process. |

## Governance

An issue MAY remain open at release only where its impact is disclosed and it does not invalidate the feature-complete claim. Issues that affect safety, internal consistency, publication integrity or the truthfulness of a conformance claim MUST block release or be governed through an explicit exception and risk-acceptance record.
