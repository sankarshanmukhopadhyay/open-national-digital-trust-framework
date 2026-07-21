# Changelog

## [0.4.0] - 2026-07-21

### Added
- deployment-neutral reference architecture and architecture principles
- architecture viewpoints, logical component and service catalogues
- trust-boundary, federation, resilience and deployment-neutrality specifications
- expanded canonical information architecture and lifecycle models
- ten canonical end-to-end workflows
- machine-readable architecture and information-model catalogues
- dedicated diagram catalogue and authoring rules


## [0.3.0] - 2026-07-21

### Added

- self-contained ONDTF core specification;
- capability catalogue and initial normative requirements;
- scoped, technology-neutral conformance model;
- machine-readable core requirements register;
- national digital trust target operating model;
- institutional function and decision-rights models;
- trust-scheme and participant lifecycle specifications;
- policy-change, oversight, transparency, redress, and maturity guidance;
- GitHub Pages navigation and site-map coverage for all new content.

## Unreleased

### Fixed

- Configure Mermaid CLI to launch Chromium with GitHub Actions-compatible no-sandbox arguments, resolving diagram-render validation failures on Ubuntu runners.
- Move documentation workflows to Node.js 24 to avoid the GitHub Actions Node.js 20 deprecation path.

## [0.2.0] - 2026-07-21

### Added

- programme charter, integrated workplan, decision rights, and evidence-based quality gates;
- canonical TSMM v0.23.0 semantic crosswalk and TIS v0.12.0 artefact adoption matrix;
- ONDTF concept ownership model and canonical information model;
- machine-readable TSMM binding, TIS profile, programme registers, and information-model inventory;
- complete documentation site map and project-document publication coverage;
- Mermaid syntax validation and built-site verification in CI.

### Changed

- corrected canonical links for ONDTF, TSMM, and TIS throughout the framework;
- strengthened GitHub Pages navigation and publication controls;
- advanced the repository to the Semantic and Portfolio Alignment Draft.

## [Unreleased]

### Changed

- Made the ONDTF core self-contained and implementation-neutral.
- Reclassified TSMM and TIS as optional compatible reference resources.
- Added outcome-based conformance and explicit profile dependency rules.
- Added ADR 0004 documenting the framework-independence decision.
- Corrected labelled dotted-edge syntax in Mermaid diagrams.
- Hardened browser-side Mermaid rendering and error reporting.

### Fixed

- Replaced the legacy `github-pages` and remote-theme dependency chain with a current Jekyll 4 and Just the Docs toolchain.
- Removed the Ruby 3.3-incompatible Jekyll 3.6/Kramdown 1.14 dependency path that failed while loading `rexml/parsers/baseparser`.
- Pinned Ruby 3.3 consistently across documentation workflows.

## [0.1.0] — 2026-07-21

### Added

- Rebuilt the seed as the Open National Digital Trust Framework.
- Established a jurisdiction-neutral core and India profile skeleton.
- Defined explicit ONDTF, TSMM, and TIS responsibility boundaries.
- Added foundations, assurance, adoption, jurisdiction-profile, decision-record, dependency, and roadmap material.
- Added architecture, governance, profile, and adoption diagrams rendered with Mermaid.
- Added repository validation and GitHub Pages quality workflow.
