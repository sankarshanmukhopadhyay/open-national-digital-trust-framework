---
title: ADR 0004 — Framework Independence
parent: Architecture Decisions
nav_order: 4
---
# ADR 0004: Keep ONDTF independent of optional technical foundations

**Status:** Accepted

## Context

ONDTF is intended to be a reusable baseline for jurisdictions and sectors with different legal systems, technical estates, standards strategies, and institutional constraints. Making TSMM, TIS, or any other external project a prerequisite would increase conceptual and implementation overhead and could constrain adoption.

## Decision

ONDTF shall maintain a self-contained core vocabulary, architecture, governance model, and outcome-based conformance framework.

TSMM and TIS are classified as optional compatible resources. Crosswalks and bindings are informative unless a named jurisdiction, sector, or technical profile explicitly selects them.

Core ONDTF conformance shall not require adoption of a particular meta-model, schema family, protocol suite, registry implementation, or software stack.

## Consequences

- ONDTF must define enough semantics to be understood independently.
- Compatibility artefacts remain valuable but cannot create implicit core dependencies.
- Profiles must clearly distinguish inherited ONDTF requirements from optional technology selections.
- Conformance focuses on observable outcomes, behaviour, and evidence.
- Alternative models and schemas can be used where they preserve required semantics and satisfy the declared profile.
