---
layout: default
title: ADR-0007 — Multidimensional Risk-based Assurance
parent: Architecture Decisions
nav_order: 7
---
# ADR-0007: Multidimensional risk-based assurance

- **Status:** Accepted
- **Decision date:** 2026-07-25
- **Applies from:** ONDTF v0.6.x

## Context

The former A0–A3 shorthand combined decision consequence, control strength, assessment independence and operational confidence. This created a risk that an aggregate label would conceal a failed critical dimension or be misrepresented as general trustworthiness.

Current assurance practice separates functional assurance, risk context, assessment rigour, conformance and lifecycle state. ONDTF also covers authority, delegation, execution, privacy, operational resilience and remedy beyond digital identity assurance.

## Decision

ONDTF will represent assurance as a context-bounded vector comprising:

1. Decision Impact Class;
2. dimension-specific assurance requirements;
3. achieved dimension results;
4. Evaluation Rigour Class;
5. evidence freshness and validity;
6. current assurance state; and
7. blocking dimensions and reassessment triggers.

Critical dimensions use a non-compensating floor. A failed critical dimension cannot be offset by stronger results elsewhere. The A0–A3 shorthand is deprecated and has no automatic conversion.

External assurance schemes are mapped only within their native scope and version. Such mappings do not create equivalence, certification, accreditation or legal recognition.

## Consequences

- Profiles must publish explicit dimension requirements and failure actions.
- Conclusions must disclose assessment rigour, validity and blocking gaps.
- Conformance and assurance remain distinct.
- Existing A0–A3 uses require dimension-by-dimension reassessment.
- Schema validation tests both accepted and rejected assurance records.
