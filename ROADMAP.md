# Roadmap

## Released baselines

- **v0.5.0 — Feature Complete Draft:** complete architectural baseline.
- **v0.6.0 — Operational Framework Draft:** governed operational composition and sector adoption foundation.
- **v0.7.0 — Implementation and Evaluation Draft:** reference implementation, executable assurance foundation, identifier resolution and evaluation machinery.
- **v0.9.0 — Candidate Specification:** stable normative surface, complete candidate traceability, conformance classes, interoperability/recognition evidence models, candidate governance and open external review window.

## Governing release model

ONDTF now separates **specification maturity** from **evidence maturity**. Specification releases advance when repository-controlled stability, traceability, compatibility, validation and governance gates are satisfied. Independent implementation, cross-implementation interoperability and operational deployment remain stronger evidence states that constrain the claims ONDTF may make, but do not create an external veto over specification evolution.

See [Specification Maturity and Evidence Governance](docs/project/maturity-and-evidence.md) and the machine-readable [`governance/maturity.yaml`](governance/maturity.yaml).

## Forward path

### v1.0.0 — Stable Framework Specification

**Goal:** establish ONDTF as a stable normative contract that implementers and framework authorities can safely build against without implying unsupported operational maturity.

Promotion requires:

- stable normative identifiers and terminology;
- complete requirement-to-conformance traceability;
- deterministic repository validation and reproducible release integrity;
- consequential negative and adversarial test coverage;
- explicit backwards-compatibility and normative-change rules;
- active errata, emergency-change and evidence-invalidation controls;
- disposition of internally controllable blocking issues;
- explicit declaration of the current evidence maturity level and unsupported claims.

Independent implementation remains required for an `E2` evidence claim, but is not a prerequisite for specification stability.

### v1.1.x — Executable Specification

**Bold goal:** make every ONDTF requirement either machine-testable or explicitly assessor-verifiable, with no ambiguous middle category.

Target outcomes:

- 100% requirements mapped to deterministic conformance assertions or governed assessor procedures;
- machine-readable claim, evidence and decision-receipt formats for every conformance class;
- negative vectors for authority, scope, lifecycle, freshness, revocation, remedy and recognition failure;
- generated conformance coverage dashboards with zero orphan normative requirements;
- clean-room implementability harness proving that published artefacts are sufficient without maintainer-only knowledge.

### v1.2.x — Portable Framework Construction

**Bold goal:** prove that ONDTF can generate materially different national or sectoral trust-framework profiles without collapsing into a single technology or governance pattern.

Target outcomes:

- at least four independently constructed profile packages from different jurisdictional or sectoral assumptions;
- deterministic profile generation and migration across ONDTF minor versions;
- explicit conflict, strengthening, exception and non-applicability semantics;
- profile-diff tooling that exposes semantic, governance and assurance changes;
- evidence that alternative identifier, credential, registry and policy technologies can satisfy the same ONDTF capability contract.

### v1.3.x — Interoperability and Recognition Laboratory

**Bold goal:** make semantic, policy, governance and operational interoperability falsifiable even before external ecosystems participate.

Target outcomes:

- executable cross-profile interoperability matrices;
- recognition/equivalence tests with weakest-link, expiry, revocation and downgrade behaviour;
- mismatch vectors for policy, assurance, status, lifecycle, jurisdiction and version boundaries;
- reusable interoperability event packages that an external implementer can run without bespoke maintainer support;
- publication of bounded evidence claims that clearly distinguish repository simulation from external `E3` evidence.

### v1.4.x — Evidence-Native Governance

**Bold goal:** turn release governance, assurance state and evidence invalidation into executable controls rather than manual interpretation.

Target outcomes:

- machine-verifiable release gates;
- version-scoped evidence inventories with provenance, freshness, applicability and invalidation triggers;
- automatic downgrade flags when a material normative change invalidates prior evidence;
- generated release claim manifests describing what may and may not be asserted;
- audit-ready linkage from issue → decision → requirement → implementation → test → evidence → release claim.

### v1.5.x — Operational Readiness Package

**Bold goal:** make ONDTF consumable by a competent external framework authority, implementer or assessor with minimal maintainer intervention.

Target outcomes:

- implementation starter kit and assessor kit generated from the canonical model;
- bounded reference deployment patterns covering centralised, federated and delegated trust architectures;
- operational runbooks for incident, suspension, revocation, appeal, remedy and recovery;
- measurable assurance and observability expectations with uncertainty explicitly represented;
- external-evidence intake process that can admit `E2`, `E3` or `E4` evidence without changing ONDTF semantic authority.

### v2.0.0 — Only for justified semantic break

ONDTF should not target v2.0 as a calendar milestone. A major version is warranted only when evidence demonstrates that a backwards-incompatible semantic, governance, profile or conformance change is necessary and cannot be represented safely within the v1.x contract.

## Evidence ambition

The project should actively seek, but never manufacture, stronger evidence states:

```text
E0  specification evidence only
 ↓
E1  repository-controlled executable/reference evidence
 ↓
E2  independent implementation evidence
 ↓
E3  cross-implementation interoperability evidence
 ↓
E4  operational deployment evidence
```

Progress along this axis is reported independently of specification version. A future external implementation can therefore raise the evidence maturity of an existing ONDTF release without forcing an artificial specification version change.

## Roadmap operating rule

Every roadmap goal must produce at least one machine-verifiable artefact, executable test, bounded evidence record or externally reviewable conformance procedure. New conceptual surface should be admitted only when existing ONDTF semantics cannot represent a demonstrated requirement or implementation pressure.

The detailed pre-v0.9.0 delivery plan remains preserved as historical judgment in [`docs/project/detailed-delivery-roadmap.md`](docs/project/detailed-delivery-roadmap.md). It is no longer the authority for post-v0.9.0 promotion rules.
