---
layout: default
title: ADR 0006 — Governed Controlled Vocabulary
parent: Architecture Decisions
nav_order: 6
---
# ADR 0006: Governed controlled vocabulary

- **Status:** Accepted
- **Date:** 2026-07-25

## Context

ONDTF used important governance, assurance, profile, and conformance terms across the repository, but maintained only a small manual glossary. This limited semantic consistency, provenance, machine use, and release assurance. The CTWG Glossary demonstrates useful structured-governance patterns, but importing its vocabulary authority would conflict with ONDTF independence and jurisdiction-neutrality.

## Decision

ONDTF will maintain one structured YAML source record per controlled term. ONDTF definitions are authoritative within ONDTF. External vocabularies may inform or map to terms but are non-normative unless an ONDTF decision explicitly adopts them. Reader pages and machine-readable bundles are generated from the term records and validated in CI.

## Consequences

Normative terminology changes become governed specification changes. Profiles and conformance artefacts can reference stable term identifiers. Deprecation and retirement remain auditable. CI can verify structural integrity and reproducibility, while semantic equivalence and jurisdictional neutrality remain human review responsibilities.
