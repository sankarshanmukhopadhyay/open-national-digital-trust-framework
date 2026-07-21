---
layout: default
title: Deployment Neutrality
parent: Reference Architecture
nav_order: 10
---

# Deployment neutrality

ONDTF supports centralised, federated, distributed and hybrid deployments. Conformance depends on capabilities and evidence, not topology.

| Topology | Strength | Principal risk |
|---|---|---|
| Centralised | operational simplicity | concentration and capture |
| Federated | institutional autonomy | inconsistent semantics and assurance |
| Distributed | reduced single-point dependency | governance and coordination complexity |
| Hybrid | fit-for-purpose allocation | hidden coupling and unclear accountability |

An adopter MAY use PKI, controlled identifiers, DIDs, trust lists, conventional databases, distributed ledgers or equivalent mechanisms. The selected profile MUST define authoritative resolution, status, governance and recovery semantics.

## Deployment decision record

A deployment decision SHOULD document:

- capabilities allocated to each component;
- accountable and operating owners;
- trust boundaries and data flows;
- dependencies and concentration risks;
- availability and recovery targets;
- security and privacy controls;
- evidence and audit arrangements;
- exit, migration and continuity strategy.
