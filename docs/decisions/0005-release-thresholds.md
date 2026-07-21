---
layout: default
title: ADR 0005 — Release Thresholds
parent: Architecture Decisions
nav_order: 5
---

# ADR 0005: Release thresholds

- **Status:** Accepted
- **Date:** 2026-07-21

## Context

ONDTF will evolve through frequent documentation, tooling, architecture, profile, and normative changes. Treating every successful commit as a release would create noise, while withholding releases after substantive specification changes would deny adopters a stable reference point.

## Decision

ONDTF uses commit-only treatment for maintenance and non-semantic refinements, patch releases for externally material backward-compatible corrections, and minor releases for new normative, architectural, operating-model, profile, conformance, or machine-readable baselines.

Candidate and stable releases require progressively stronger review and implementation evidence.

## Consequences

The release decision must be recorded before packaging a substantive payload. GitHub Pages or Mermaid fixes alone normally remain commit-only. The introduction of the core specification and target operating model is classified as a minor release.
