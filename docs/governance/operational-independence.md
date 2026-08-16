---
layout: default
title: Operational Independence Evidence
parent: Governance
nav_order: 18
---

# Operational independence evidence

[`ONDTF-ROL-004`](../core-specification/requirements-register.md#ondtf-rol-004) requires an independent review path, while [`ONDTF-ROL-005`](../core-specification/requirements-register.md#ondtf-rol-005) prevents an operating body from being the sole assessor and final appeals body for its own material conformance decisions. A separate organisational label is not sufficient evidence of independence.

`OIEP-001` therefore defines reviewable evidence tests for:

- appointment and removal authority;
- funding and budget control;
- conflict-of-interest treatment;
- recusal;
- decision override, escalation and remedial authority;
- publication obligations; and
- structural or common-control dependence.

The canonical machine-readable tests are in `model/governance/operational-independence-evidence.yaml`.

## Negative case

A separately named review body fails the operational-independence test when it is funded, appointed and removable solely by the operating body **and** lacks effective remedial or escalation authority. The purpose of the test is to distinguish nominal separation from evidence that review can operate despite institutional pressure or conflict.
