---
layout: default
title: ADR 0001 — Jurisdiction-neutral core
nav_order: 1
---
# ADR 0001: Jurisdiction-neutral core with profiles

**Status:** Accepted for v0.1.0

## Decision

The framework is named the Open National Digital Trust Framework. The core remains jurisdiction-neutral. Country-specific requirements are maintained as profiles, beginning with India.

## Rationale

This preserves global reuse, enables comparison across jurisdictions, avoids embedding one legal system into the semantic core, and allows national adoption without forking the architecture.

## Consequences

The core cannot claim legal effect. Each jurisdiction profile must identify its own authorities, legal bases, recognition rules, and deviations.
