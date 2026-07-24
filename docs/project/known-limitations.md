---
layout: default
title: Known Limitations
parent: Project Governance and Releases
nav_order: 3
---

# Known limitations

## Purpose

This page states the boundaries that remain after the v0.6.0 Operational Framework Draft. It is a release view of the canonical [`maturation-register.yaml`](../../model/project/maturation-register.yaml), not an independent backlog. Closed maturity issues have been removed from the active limitation narrative, while enduring framework boundaries remain visible because operational maturity does not make them disappear.

| Type | Meaning |
|---|---|
| **Enduring** | A deliberate boundary that remains true even when implementation guidance is mature. |
| **Reducible** | A maturity constraint that can be reduced through implementation, evidence or review. |
| **Maintained** | A continuing governance risk controlled through review cadence and change management. |

## Active limitations at v0.6.0

| ID | Limitation | Type | Practical consequence | Related issue |
|---|---|---|---|---|
| LIM-01 | Independent implementation evidence remains limited | Reducible | Portability, implementability and interoperability claims remain provisional until independently exercised. | URI-01 |
| LIM-02 | Standards mappings are informative unless selected by a profile | Enduring | A mapping alone does not create a normative dependency or conformance obligation. | URI-07, URI-19 closed; boundary retained |
| LIM-03 | Jurisdiction profiles are implementation aids, not legal advice | Enduring | Adoption without competent current local review may misstate legal effect or authority. | URI-03 |
| LIM-04 | Quantitative thresholds require contextual calibration | Reducible | Default values may not represent sector risk, scale or operational conditions. | URI-02 |
| LIM-05 | Reference schemas, validators and fixtures are not production software | Enduring | Repository artefacts do not establish security, availability, certification or fitness for deployment. | URI-04 |
| LIM-06 | Cross-border recognition depends on external legal and institutional arrangements | Enduring | Technical compatibility cannot create legal recognition, liability allocation or reciprocal supervision. | URI-16 |
| LIM-07 | Cryptographic and protocol choices remain profile-dependent | Enduring | Core conformance does not imply protocol or cryptographic interoperability. | URI-05 |
| LIM-08 | Repository validation is not implementation or scheme conformance | Enduring | Passing repository checks cannot support a provider, product or organisational conformance claim. | URI-04 |
| LIM-09 | Standards and regulatory sources change over time | Maintained | Profiles and mappings can become stale; the v0.6.0 maintenance model controls rather than eliminates this risk. | URI-07 and URI-18 closed |

## Limitations materially reduced in this release

v0.6.0 resolves the previously open architectural gaps concerning role-specific normative obligations, provider lifecycle, institutional operating roles, accreditation and certification, profile construction, controlled-document maintenance, standards-change handling and external-pattern adoption. These matters are now governed by published documentation, machine-readable catalogues and worked-profile validation.

The release does **not** convert design evidence into deployment evidence. Accessibility, challenge, appeal and remedy now have complete operating models, but their end-to-end effectiveness still requires pilot validation. The same distinction applies to performance, adversarial exercises and cross-implementation interoperability.

## Treatment and release use

A reducible limitation must link to an owned issue, target release and closure evidence. An enduring limitation remains disclosed even after related guidance matures. A maintained limitation remains subject to source-change triggers, review cadence and migration procedures.

See the [Unresolved Issues Register](unresolved-issues.md), [Future Work](future-work.md), [Implementation Evidence Programme](implementation-evidence.md) and [v0.6.0 Readiness Checklist](v0.6-readiness-checklist.md).
