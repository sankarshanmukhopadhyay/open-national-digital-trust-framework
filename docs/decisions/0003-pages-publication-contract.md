---
title: ADR 0003 — GitHub Pages Publication Contract
parent: Architecture Decisions
nav_order: 3
---
# ADR 0003 — GitHub Pages Publication Contract

## Status

Accepted.

## Decision

All human-readable ONDTF documentation must be reachable from the GitHub Pages navigation or documentation site map. Mermaid diagrams must be rendered client-side by a pinned Mermaid version and syntax-validated in continuous integration. Machine-readable artefacts remain repository files and must have corresponding explanatory documentation.

## Consequences

Every new Markdown page requires valid front matter, a stable title, and publication coverage. CI must build the site, validate links, validate front matter and navigation coverage, check Mermaid syntax, and inspect the generated site for unresolved Mermaid blocks or broken internal references.
