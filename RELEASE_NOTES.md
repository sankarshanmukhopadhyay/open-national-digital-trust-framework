# Release notes

## v0.4.0 — Reference Architecture and Information Architecture Draft

This release converts the ONDTF core capabilities and target operating model into a deployment-neutral reference architecture. It introduces architecture principles, layered and plane models, viewpoints, logical components, services, trust boundaries, federation, resilience, canonical information semantics and governed workflows.

### Reference architecture

- establishes twelve architecture principles;
- defines thirteen architectural layers and six cross-cutting planes;
- introduces policy, governance, implementation, assurance, affected-party and federation viewpoints;
- defines eighteen logical components and eighteen protocol-neutral services;
- establishes a catalogue of twenty canonical interactions;
- defines trust-boundary crossing and cross-domain recognition requirements;
- adds safe-failure, resilience and deployment-neutrality guidance.

### Information architecture and workflows

- defines twenty-eight canonical entities and core relationships;
- introduces lifecycle, decision-state, identifier, provenance and information-governance rules;
- adds ten detailed canonical workflows from scheme establishment through conformance declaration;
- publishes machine-readable architecture, component, service, boundary, interaction and entity catalogues.

### Publication quality

All new pages are included in GitHub Pages navigation and site-map coverage. Mermaid diagrams are source-validated, extracted and rendered with the pinned CLI in CI before the site build.

### Release status

This is an initial public draft and not a candidate or stable specification. The architecture is sufficiently substantive to establish a minor-version baseline for later security, assurance, profile and conformance work.

## v0.3.0 — Core Specification and Operating Model Draft

This release moves ONDTF from repository and semantic foundations into its first coordinated specification baseline. It defines what an adopting national digital trust framework is expected to achieve while preserving implementation and technology independence.

### Core specification

- establishes the scope and explicit non-goals of ONDTF;
- introduces a compact, self-contained conceptual baseline;
- defines fifteen outcome-oriented national digital trust capabilities;
- introduces the first normative requirement set across governance, authority, delegation, evidence, assurance, decisions, security, privacy, incidents, redress, interoperability, and conformance;
- defines scoped conformance classes and prohibits unqualified “ONDTF compliant” claims;
- preserves the principle that core conformance does not depend on TSMM, TIS, or any particular technology stack;
- introduces a machine-readable requirements register and traceability method.

### National digital trust target operating model

- defines essential institutional functions without prescribing a single agency structure;
- establishes decision-right and delegation requirements;
- introduces governed trust-scheme and participant lifecycles;
- defines standard and emergency policy-change processes;
- establishes transparency and independent oversight expectations;
- operationalises challenge, correction, appeal, remedy, and systemic learning;
- introduces a capability-based maturity model for staged adoption.

### Publication quality

All new documentation is included in GitHub Pages navigation and the documentation site map. Mermaid source validation and authoritative Mermaid CLI rendering remain mandatory in CI before the Just the Docs site is built.

### Release status

This is a public draft. It is sufficiently substantive to warrant a minor-version release because it introduces a new normative baseline and target operating model that downstream profiles and future conformance work will reference. It is not a candidate or stable specification.
