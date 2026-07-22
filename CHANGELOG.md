# Changelog

## [Unreleased]

### Added

- operational risk methodology, assurance evidence model, evaluation conclusions and conformance assessment workflow;
- continuous assurance, trust observability, resilience, exception handling and metrics guidance;
- machine-readable risk, conformance, standards-register and NIST CSF mapping artefacts;
- standards reference policy and initial alignment with ISO 31000, ISO/IEC 27001, ISO/IEC 27002, ISO/IEC 27005, NIST CSF 2.0, NIST SP 800-53, NIST SP 800-37 and ISO/IEC 17000-series concepts.

### Fixed

- replaced the duplicate custom Mermaid browser runtime with the native Just the Docs Mermaid integration;
- pinned Just the Docs to the current 0.12 release line and added native Mermaid configuration;
- strengthened built-site validation to verify Mermaid runtime inclusion and reject legacy render-error placeholders.


### Added

- Structured threat taxonomy, adversary catalogue, attack-surface catalogue, and 48 stable threat records.
- Security control framework with eight control families and 40 stable controls.
- Worked delegated-eligibility reference scenario with ten reusable evidence fixtures and threat-to-control traceability.
- Machine-readable security catalogues supporting later risk scoring, assurance evidence, and conformance work.

### Fixed

- Aligned authoritative ONDTF repository metadata with the released `0.4.0` baseline.
- Completed the machine-readable decision register for ADR-0004 and ADR-0005.
- Added protected asset `AST-21` for automated-agent mandates and tool-invocation records and linked it to `SB-19`.
- Resolved Just-the-Docs navigation-order collisions while preserving superseded public routes through non-navigational migration pages.
- Extended repository validation for navigation uniqueness, authoritative version consistency, binding identifier/version coherence, ADR completeness, and security-domain traceability.


### Added

- established the ONDTF security architecture foundation, including twelve security principles, twelve security objectives, twelve security domains, and an explicit trust-assumption model;
- added a machine-readable security-foundations catalogue for future threat, control, assurance, and metric traceability.
- added a canonical protected-asset catalogue spanning institutional, authority, semantic, operational, accountability, privacy, and continuity assets;
- added a security-boundary model with twenty-two stable boundary identifiers, crossing requirements, lifecycle states, evidence obligations, and failure modes;
- added AST-21 (automated-agent mandates and tool-invocation records) so SEC-DOM-12 has protected-asset and boundary traceability;
- added repository validation checks for nav_order uniqueness per navigation parent, framework self-version consistency across VERSION/PROJECT-STATUS/CITATION.cff/README/bindings/dependencies, decision-register completeness against published ADRs, and security-domain-to-asset traceability.

### Changed

- corrected the documentation site map to generate base-path-aware published URLs instead of links to Markdown source files;
- corrected numbered Mermaid node labels in the layered reference architecture that were interpreted as unsupported Markdown lists;
- separated the Security Architecture publication section from the independent Assurance section and expanded repository-wide navigation for the developing v0.5.0 baseline;
- registered ADR-0004 and ADR-0005 in `governance/decision-register.yaml`, which previously only listed ADR-0001 through ADR-0003;
- renumbered colliding `nav_order` values across the top-level navigation, Foundations, Security Architecture, Reference Architecture, and Information Architecture sections so every page has a stable, unambiguous sidebar position.

### Fixed

- corrected the ONDTF self-version declared in `data/dependencies.yaml` (was 0.3.0) and in `bindings/tis/ondtf-tis-profile.json` and `bindings/tsmm/ondtf-tsmm-binding.json` (both were 0.2.0, including their URN identifiers) to match the actual repository version, 0.4.0;
- removed seven orphaned pre-catalogue documentation pages (`docs/information-model/entities.md`, `identifiers-provenance.md`, `lifecycle.md`; `docs/architecture/trust-model.md`, `actor-model.md`, `lifecycle.md`, `reference-stack.md`) that had been superseded by their ID-based canonical replacements but were never retired, and that had no inbound links;
- consolidated three duplicate `## Unreleased` sections in this changelog into the release entries they actually shipped with.

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
- advanced the repository to the Semantic and Portfolio Alignment Draft;
- Made the ONDTF core self-contained and implementation-neutral;
- Reclassified TSMM and TIS as optional compatible reference resources;
- Added outcome-based conformance and explicit profile dependency rules;
- Added ADR 0004 documenting the framework-independence decision;
- Corrected labelled dotted-edge syntax in Mermaid diagrams;
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
