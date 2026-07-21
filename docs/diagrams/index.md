---
layout: default
title: Diagram Catalogue
parent: Open National Digital Trust Framework
nav_order: 98
---

# Diagram catalogue

All Mermaid diagrams in published Markdown are extracted and rendered with Mermaid CLI during continuous integration. A workflow fails if any diagram cannot be parsed or rendered.

## Authoring rules

- use supported Mermaid declarations only;
- prefer simple quoted labels where punctuation is necessary;
- use `-.->|label|` for labelled dotted edges;
- avoid raw HTML and escaped newline sequences in node labels;
- keep identifiers alphanumeric;
- test every diagram through the repository validation workflow.

## Architecture diagrams

The reference architecture includes plane, layer, viewpoint, component-separation, interaction, trust-boundary, federation and resilience diagrams. The information architecture includes class, relationship, lifecycle and provenance diagrams. Canonical workflows include sequence, flow and state diagrams.

Rendered SVG artefacts are retained by CI to support diagnosis of browser-side rendering differences.
