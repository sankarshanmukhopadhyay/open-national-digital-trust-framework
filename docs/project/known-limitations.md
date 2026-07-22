---
layout: default
title: Known Limitations
parent: Project Governance and Releases
nav_order: 3
---

# Known limitations

## Purpose

This page describes what ONDTF deliberately does not yet claim or provide. It is a coordinated view of the canonical [`maturation-register.yaml`](../../model/project/maturation-register.yaml), not a separate backlog. Some limitations are permanent framework boundaries; others can be reduced through implementation evidence; a third group requires continuing maintenance.

| Type | Meaning |
|---|---|
| **Enduring** | A deliberate boundary that should remain visible and is not expected to disappear. |
| **Reducible** | A maturity constraint that can be reduced through implementation, evidence or review. |
| **Maintained** | A continuing governance risk requiring periodic review and change control. |

## Current limitations

| ID | Limitation | Type | Practical consequence | Related issue |
|---|---|---|---|---|
| LIM-01 | Independent implementation evidence remains limited | Reducible | Portability, implementability and interoperability claims remain provisional. | URI-01 |
| LIM-02 | Standards mappings are informative unless selected by a profile | Enduring | A mapping alone does not create a normative dependency or conformance obligation. | URI-07, URI-19 |
| LIM-03 | Jurisdiction profiles are implementation aids, not legal advice | Enduring | Adoption without competent local review may misstate legal effect or authority. | URI-03 |
| LIM-04 | Quantitative thresholds require contextual calibration | Reducible | Default values may not represent sector risk or operational conditions. | URI-02 |
| LIM-05 | Reference schemas and fixtures are not production software | Enduring | Repository artefacts do not establish security, availability or fitness. | URI-04 |
| LIM-06 | Cross-border recognition depends on external legal and institutional arrangements | Enduring | Technical compatibility does not create legal recognition or liability allocation. | URI-16 |
| LIM-07 | Cryptographic and protocol choices remain profile-dependent | Enduring | Core conformance does not imply protocol interoperability. | URI-05, URI-12 |
| LIM-08 | Repository validation is not implementation or scheme conformance | Enduring | Passing repository checks cannot support a provider or organisational conformance claim. | URI-04, URI-09 |
| LIM-09 | Standards and regulatory sources change over time | Maintained | Profiles and mappings may become stale or materially inaccurate. | URI-07, URI-18 |

## How limitations are treated

A reducible limitation must link to a tracked issue with an owner, target release and closure evidence. An enduring limitation remains disclosed even after associated operating guidance is mature. A maintained limitation remains subject to review cadence, source-change triggers and migration procedures.

Mitigations, issue ownership and closure criteria are maintained in the [Unresolved Issues Register](unresolved-issues.md). Planned resolution work is grouped in [Future Work](future-work.md). Proven external patterns that may address a limitation are governed through [External Framework Pattern Adoption](external-framework-pattern-adoption.md).
