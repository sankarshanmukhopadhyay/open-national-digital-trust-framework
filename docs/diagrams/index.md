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

## GitHub Pages rendering contract

ONDTF uses the native Mermaid integration supplied by the pinned **Just the Docs** theme. The site-level `mermaid.version` setting in `_config.yml` enables the theme component, while `_includes/mermaid_config.js` contains the supported runtime configuration.

The repository **MUST NOT** add a second Mermaid script tag or a separate browser-side initializer through `head_custom.html`, a custom layout, or another asset. Competing loaders can initialize different Mermaid builds against the same fenced blocks and can prevent every diagram on the published site from rendering.

The documentation pipeline therefore applies three distinct checks:

1. source validation rejects unsupported or malformed Mermaid constructs;
2. Mermaid CLI renders every extracted diagram during continuous integration;
3. built-site validation confirms that every source diagram becomes a `language-mermaid` block and that the Just the Docs Mermaid import and initializer are present on every generated page.

A change to the Mermaid version, theme, runtime configuration, Jekyll theme, or page layout should be treated as a documentation-platform change and tested across the complete diagram catalogue before merge.
