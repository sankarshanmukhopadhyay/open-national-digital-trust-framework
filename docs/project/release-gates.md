---
layout: default
title: Maturation Release Gates
parent: Project Governance and Releases
nav_order: 14
---

# Maturation release gates

Release numbers describe evidence and stability milestones, not an entitlement to add new foundational domains.

| Release | Milestone | Required result |
|---|---|---|
| **v0.6.0** | Operational Framework Draft | Core role obligations, operating model, conformance architecture, profile kit and external-pattern governance are published and internally traceable. |
| **v0.7.0** | Implementation and Evaluation Draft | At least one independent implementation, executable baseline tests, exercise evidence and reviewed user journeys are available. |
| **v0.8.0** | Interoperability and Recognition Draft | Multi-implementation results, calibrated evidence, tested recovery and a recognition profile are available. |
| **v0.9.0** | Candidate Specification | Normative language is stable, high-severity issues are closed or formally accepted, traceability is complete, independent implementations exist and change control is credible. |

The canonical gate records and associated issue identifiers are maintained in [`model/project/maturation-register.yaml`](../../model/project/maturation-register.yaml).

## Gate discipline

A release gate is satisfied by evidence, not by page count. Deferred work must remain visible, carry an owner and have an explicit effect on release claims. A safety, internal-consistency, publication-integrity or truthful-conformance issue blocks a milestone unless an authorised exception and risk-acceptance decision is recorded.
