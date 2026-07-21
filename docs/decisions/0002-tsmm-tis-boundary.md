---
title: ADR 0002 — TSMM and TIS Boundary
parent: Architecture Decisions
nav_order: 2
---
# ADR 0002: Preserve TSMM and TIS authority boundaries

**Status:** Superseded by [ADR 0004](0004-framework-independence.md)

## Original decision

ONDTF used TSMM as a semantic foundation and TIS as a portable schema-contract foundation while preserving their independent authority.

## Supersession

Experience during the v0.2.0 alignment work showed that describing either project as a foundation could be understood as making it a prerequisite for ONDTF adoption. ADR 0004 replaces that coupling with a self-contained ONDTF core and optional compatibility profiles.
