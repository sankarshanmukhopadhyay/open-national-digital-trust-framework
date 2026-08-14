---
layout: default
title: Candidate Review Programme
parent: Project Governance and Releases
nav_order: 25
---
# Candidate review programme

Review comments use stable `REV-*` identifiers and one of: editorial, technical, governance, rights, security, interoperability or blocking. Each comment records scope, affected artefacts, disposition, rationale, required tests and whether implementation evidence must be rerun.

## Protocol

1. Freeze the review package and candidate version.
2. Record every material review comment in the review register.
3. Classify and assign ownership.
4. Resolve, reject with rationale, or defer with explicit candidate effect.
5. Rerun impacted validation and interoperability evidence.
6. Publish the disposition record before v1.0.0 promotion.

The repository ships a review-ready protocol and empty external-review intake surface; it does not fabricate external reviewer participation.
