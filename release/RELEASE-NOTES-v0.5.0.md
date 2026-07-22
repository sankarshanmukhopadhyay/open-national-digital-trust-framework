# ONDTF v0.5.0 — Feature Complete Draft

**Release date:** 2026-07-22

## Executive summary

v0.5.0 establishes the complete planned architectural baseline of the Open National Digital Trust Framework. ONDTF now connects governance, identity, authority, delegation, policy, evidence, assurance, decision, effect, accountability, privacy, rights, interoperability, and remedy within one jurisdiction-neutral framework.

“Feature Complete Draft” means the foundational capability surface is present and integrated. It does not mean the framework is a candidate specification, a legal determination, a certified implementation, or a substitute for jurisdiction and sector profiles. The next development cycle is intentionally implementation-led.

## Release highlights

- Complete governance, authority, reference architecture, and information architecture baseline.
- Integrated security architecture with protected assets, trust boundaries, adversaries, attack surfaces, threats, and controls.
- Operational risk, assurance, conformance, continuous assurance, metrics, and resilience guidance.
- Dedicated data-security, privacy, affected-party, challenge, appeal, remedy, and accountability architecture.
- Jurisdiction-profile method, cross-border guidance, and informative India profile.
- Consolidated register of 46 standards, specifications, guidelines, and jurisdictional instruments with stable local citation anchors.
- Worked end-to-end reference scenario, machine-readable catalogues, schemas, fixtures, and traceability artefacts.
- Role-based learning paths, GitHub Pages publication, Mermaid diagrams, responsive standards table, and built-site link validation.

## Architectural milestone

This release is the point at which ONDTF moves from architectural expansion to validation and maturation. Future work should normally improve clarity, evidence semantics, interoperability, deployability, conformance, and review outcomes rather than introduce additional foundational domains.

## Security, assurance, privacy, and rights

v0.5.0 treats these as coordinated but distinct architectural concerns. Security controls do not substitute for privacy safeguards; privacy does not establish authority; authentication does not prove valid delegation; and audit does not by itself create challenge or remedy. The framework therefore links preventive, detective, corrective, and compensating controls to evidence, decisions, affected parties, oversight, and operational recovery.

## Standards alignment

The release maintains a single canonical register for standards and instruments used throughout ONDTF. Each registered item has a stable identifier, publisher, title, status, classification, intended use, canonical source, and review date. Local citations resolve to the register so that references can be maintained centrally without duplicating edition metadata across the framework.

## Release scale

- **190** published documentation and profile pages
- **96** Mermaid diagrams
- **46** registered standards and instruments
- **56** YAML, YML, and JSON artefacts
- **9** repository scripts

## Validation

The release payload includes repository, standards-reference, data/privacy/rights, integration, Mermaid-source, Mermaid-rendering, Jekyll-build, and built-site checks. The GitHub Pages deployment and release tag must be verified after the release commit is merged.

## Known limitations

- Reference artefacts are not a complete executable conformance suite.
- Jurisdiction profiles require current local legal and regulatory review.
- Independent implementation and cross-vendor interoperability evidence remain limited.
- Assurance levels and evidence thresholds require further pilot validation.
- ONDTF does not itself create legal recognition, regulatory approval, or production certification.

See [Known Limitations](../docs/project/known-limitations.md) and [Unresolved Issues](../docs/project/unresolved-issues.md).

## Upgrade notes

No automated migration is required from v0.4.0. Adopters should review the new security, assurance, privacy, rights, standards, jurisdiction, and reference-scenario material; update profile declarations; and scope any conformance claim to v0.5.0 and the applicable profile.

## Looking ahead

The v0.6.x cycle focuses on implementation refinement. Later cycles add deployment evidence, stronger interoperability and conformance, external review, and candidate-specification hardening on the path to v0.9.0 and v1.0.0.
