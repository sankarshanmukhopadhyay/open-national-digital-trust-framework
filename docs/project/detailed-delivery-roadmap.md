---
layout: default
title: Detailed Delivery Roadmap to v0.9.0
parent: Project Governance and Releases
nav_order: 17
---
# ONDTF Detailed Delivery Roadmap: Current State to v0.9.0 Candidate Specification

**Document status:** Planning baseline  
**Starting point:** Repository state following introduction of governed profiles and ONDTF Guided Framework Construction  
**Target state:** `v0.9.0 — Candidate Specification`  
**Intended audience:** maintainers, specification editors, implementers, profile authors, assessors, reviewers, governance authorities, pilot partners, and release managers

## 1. Purpose

This roadmap defines a straight, evidence-led path from the current ONDTF repository state to a credible `v0.9.0 Candidate Specification` release.

The central objective is not to add more conceptual surface area. The repository already contains a broad architectural model, institutional roles, provider lifecycle, conformance concepts, multidimensional assurance, rights and remedy, governed profiles, and a guided framework-construction capability. The remaining work is to transform that breadth into a specification that is operationally demonstrable, independently implementable, interoperable across at least two implementations, governed through stable change controls, and sufficiently mature for candidate-specification review.

The progression should therefore follow this logic:

```text
operational completeness
→ executable implementation evidence
→ independent conformance evidence
→ interoperability evidence
→ calibrated assurance and rights evidence
→ controlled normative stabilisation
→ candidate specification
```

The plan treats each release as an evidence gate rather than a feature milestone.

## 2. Release progression

| Release | Working designation | Core question answered |
|---|---|---|
| `v0.6.0` | Operational Framework Draft | Can ONDTF produce a coherent, complete and internally validated operational DTF? |
| `v0.7.0` | Implementation and Evaluation Draft | Can independent implementers build and assess against it? |
| `v0.8.0` | Interoperability and Recognition Draft | Can independent implementations interoperate and can external trust relationships be governed? |
| `v0.9.0` | Candidate Specification | Is the normative core stable, traceable, reviewable and ready for final implementation feedback? |

## 3. Current-state baseline

The current repository is assumed to contain the following capabilities:

- a canonical maturation register;
- normative requirement conventions and machine-readable requirement records;
- institutional roles and responsibility assignments;
- provider and trust-service lifecycle models;
- conformance, accreditation and certificate-status models;
- multidimensional assurance with critical-dimension floors;
- affected-party rights, challenge, appeal, remedy and accessibility models;
- governed jurisdiction, sector, technology, recognition and operational profiles;
- external-pattern adoption and dependency governance;
- controlled-document and maintenance policies;
- ONDTF Guided Framework Construction, including question, pattern, contradiction and completeness models;
- documentation architecture, learning paths, previous/next navigation and repository validation.

This baseline is architecturally strong but still carries the maturity limitations expected of a feature-complete draft:

- limited independent implementation evidence;
- no complete executable conformance suite;
- no demonstrated cross-implementation interoperability;
- incomplete empirical calibration of thresholds and operational expectations;
- limited validation of rights and remedy through realistic journeys;
- incomplete recognition and equivalence evidence;
- terminology and normative-text stability not yet demonstrated through candidate review.

## 4. Delivery principles

### 4.1 Evidence before claims

No maturity claim should be advanced merely because documentation exists. Each release gate must cite artefacts, test results, review records, decision receipts or operational evidence.

### 4.2 One canonical model, multiple views

Machine-readable models remain canonical where they already govern requirements, roles, lifecycle, profiles, construction questions, issues or release gates. Human-readable documents should remain coordinated editorial views rather than parallel sources of truth.

### 4.3 Preserve the guided-learning architecture

Every new major capability must be incorporated into:

- the canonical reading order;
- role-based learning paths;
- the repository site map;
- previous/next navigation;
- cross-links from concept to implementation and evidence;
- glossary and terminology surfaces;
- generated or maintained reference indexes.

### 4.4 Keep core and profile responsibilities distinct

The core specification defines invariant governance and assurance expectations. Profiles select jurisdictional, sectoral, technical and recognition details. Profiles may specialise or strengthen requirements but must not silently weaken mandatory core obligations.

### 4.5 Maintain technology neutrality

Reference implementations and fixtures may select concrete technologies, but the core specification must not become dependent on one identifier, credential, cryptographic or registry stack unless such a dependency is explicitly profiled.

### 4.6 Make unresolved matters visible

Unresolved questions, failed tests, uncalibrated thresholds and incomplete review must remain explicit. Candidate status should mean controlled and reviewable, not falsely complete.

## 5. Workstream structure

The programme should be managed through ten coordinated workstreams.

| Workstream | Scope |
|---|---|
| WS-1 Normative specification | requirement completeness, terminology, applicability, traceability and stability |
| WS-2 Guided construction and profiles | generated DTF packages, profile composition, validation and adopter experience |
| WS-3 Reference implementation | executable components, APIs, state models, fixtures and example deployments |
| WS-4 Conformance | test assertions, evidence records, assessor guidance, claims and certification lifecycle |
| WS-5 Interoperability and recognition | cross-implementation testing, equivalence, trust lists, status and recognition profiles |
| WS-6 Assurance and calibration | metrics, thresholds, freshness, resilience, incident and performance evidence |
| WS-7 Rights and remedy | affected-party journeys, accessibility, challenge, appeal, correction and remedy execution |
| WS-8 Governance and maintenance | document control, issue closure, change governance, dependency maintenance and release gates |
| WS-9 Documentation and learning | navigation, learning paths, diagrams, examples, tutorials and publication quality |
| WS-10 Sectoral standards adoption | sector taxonomy, capability mapping, adoption decisions, evidence obligations, maintenance and retirement |

Each release section below identifies which workstreams lead or support the work.

# Part I — v0.6.0 Operational Framework Draft

## 6. Release objective

`v0.6.0` should establish that ONDTF can be used to construct a coherent operational trust framework package from governed decisions, and that the resulting package is internally consistent across governance, lifecycle, assurance, conformance, rights, risk and maintenance.

The release should not claim production readiness or interoperability. Its claim is narrower:

> ONDTF provides a complete operational method and a worked, machine-verifiable DTF package demonstrating how the method composes.

## 7. v0.6.0 release deliverables

### 7.1 Complete worked operational profile

Create one fully worked operational profile, preferably a **National Digital Credential and Delegated Authority Service Profile** or similarly representative scenario.

The profile must include:

- purpose, scope and exclusions;
- authority basis and institutional legitimacy;
- governance bodies and decision rights;
- participant and affected-party classes;
- provider admission and service activation;
- provider and service lifecycle states;
- assurance dimensions and minimum levels by use case;
- critical non-compensable dimensions;
- conformance claim type and assessment route;
- registry, trust-list and status expectations;
- incident and emergency decision processes;
- notice, explanation, challenge, correction, appeal and remedy;
- accessibility and alternative channels;
- recognition posture;
- controlled documents, owners and review periods;
- risk, dependency, decision and unresolved-issue registers.

The profile should be produced through the Guided Framework Construction model rather than manually assembled as an unrelated example.

### 7.2 Guided construction generator, minimum viable implementation

Implement a deterministic generator that accepts a validated response file and produces the DTF package structure.

Minimum outputs:

```text
dtf-profile/
  README.md
  scope-and-purpose.md
  governance-model.md
  institutional-roles.md
  participant-obligations.md
  provider-lifecycle.md
  assurance-model.md
  conformance-model.md
  registry-and-status-model.md
  privacy-rights-and-remedy.md
  risk-and-adversarial-model.md
  recognition-and-interoperability.md
  maintenance-and-change-control.md
  unresolved-decisions.md
  model/
    profile.yaml
    roles.yaml
    requirements.yaml
    lifecycle.yaml
    assurance.yaml
    conformance.yaml
    dependencies.yaml
    risk-register.yaml
    decision-register.yaml
    review-register.yaml
```

The generator must:

- preserve answer provenance;
- distinguish selected, inherited, defaulted, provisional and unresolved values;
- apply conditional branching;
- run contradiction rules;
- apply stage completeness gates;
- generate review obligations;
- refuse to mark a package complete when blocking contradictions remain;
- emit a generation manifest recording source versions and timestamps.

### 7.3 Generated-package validation

Add validation that checks:

- all required generated files exist;
- every generated section maps to source decisions;
- every mandatory core requirement is inherited, specialised or explicitly marked with a permitted disposition;
- profile choices do not silently weaken the core;
- role references resolve;
- lifecycle transitions reference valid states and responsible roles;
- assurance requirements reference defined dimensions and levels;
- conformance claims reference an assessment route;
- rights and remedy paths identify responsible bodies;
- unresolved decisions are included in release status;
- all dependencies identify version, effect and maintenance owner.

### 7.4 Operational scenario corpus

Create a scenario corpus that exercises the worked profile end to end.

Minimum scenarios:

1. provider application and due diligence;
2. approval, registration and service activation;
3. successful delegated-authority transaction;
4. expired or revoked authority evidence;
5. registry or status endpoint unavailable;
6. material provider change requiring reassessment;
7. nonconformity and corrective action;
8. emergency suspension;
9. stale public listing after suspension;
10. affected-party challenge and evidence correction;
11. independent appeal;
12. remedy execution and downstream propagation;
13. orderly provider exit;
14. recognised external provider with constrained scope;
15. profile dependency update requiring impact review.

Each scenario should include:

- preconditions;
- participating roles;
- affected parties;
- triggering event;
- expected decisions;
- required evidence;
- generated records;
- failure outcomes;
- applicable requirements;
- review questions.

### 7.5 Operational traceability matrix

Produce a matrix linking:

```text
scenario
→ construction decision
→ generated profile provision
→ normative requirement
→ responsible role
→ evidence artefact
→ conformance assertion
→ issue or risk
```

This matrix will later seed executable test coverage.


### 7.7 Sectoral standards-adoption foundation

Establish the governed foundation for sector-specific standards adoption without claiming that any sector profile is complete or regulator-approved.

Deliver:

- a controlled sector taxonomy with stable identifiers and extensible sub-sector support;
- a controlled adoption-state and adoption-mode taxonomy;
- a sector-standard mapping model that separates relevance from formal adoption;
- an adoption decision method covering selected scope, exclusions, rationale, evidence, conflicts, approving authority, review owner and retirement triggers;
- initial illustrative mappings for public services and financial services;
- validation that rejects unknown standards, sectors, adoption states and unsupported normative claims;
- publication guidance showing standards by sector, lifecycle function, capability and adoption disposition.

The v0.6.0 claim is limited to architectural and governance readiness. Pilot validation, sector-authority approval and empirical adoption evidence remain later-release work.

### 7.8 Release documentation

Create:

- `release/RELEASE-NOTES-v0.6.0.md`;
- `release/MANIFEST-v0.6.0.md`;
- `release/DOCUMENT-INVENTORY-v0.6.0.md`;
- `release/REQUIREMENTS-INVENTORY-v0.6.0.md`;
- `release/EVIDENCE-INVENTORY-v0.6.0.md`;
- `release/CHECKLIST-v0.6.0.md`.

Update:

- `VERSION`;
- changelog;
- implementation status;
- known limitations;
- unresolved issues;
- future work;
- maturation register;
- release gates;
- adoption roadmap.

## 8. Recommended v0.6.0 commit sequence

### Commit A — Worked profile decision baseline

**Title:** `feat: define the worked operational trust framework profile`

Deliver:

- completed guided-construction response set;
- decision register;
- profile manifest;
- institutional and scope decisions;
- unresolved-decision list;
- review status for every material answer.

Acceptance criteria:

- all construction stages have a status;
- blocking contradictions are resolved or formally recorded;
- authority and amendment rights are explicit;
- all role combinations are checked against separation-of-duty constraints.

### Commit B — Framework construction generator

**Title:** `feat: generate governed DTF packages from construction decisions`

Deliver:

- generator script or library;
- templates;
- generation manifest;
- deterministic-output tests;
- schema validation;
- generated worked profile.

Acceptance criteria:

- repeated generation from the same inputs yields semantically identical output;
- manually editing generated files is either prevented or clearly marked as unsupported;
- all output sections cite their source decision identifiers.

### Commit C — Operational scenario and evidence corpus

**Title:** `test: add operational scenarios and evidence fixtures`

Deliver:

- scenario catalogue;
- positive and adverse cases;
- evidence examples;
- decision records;
- incident, challenge, appeal and remedy fixtures.

Acceptance criteria:

- every major lifecycle state is exercised;
- every critical assurance dimension appears in at least one failure scenario;
- rights and remedy are exercised in more than one scenario;
- affected parties are explicitly represented.

### Commit D — Integrated validation and traceability

**Title:** `test: validate generated profiles and operational traceability`

Deliver:

- generated-package validator;
- traceability-matrix generator;
- broken-reference and stale-model checks;
- CI integration.

Acceptance criteria:

- no orphan requirements, roles, questions, profile provisions or evidence records;
- no profile weakening without explicit permitted disposition;
- no release gate can pass with unresolved blockers.

### Commit E — Sectoral standards-adoption foundation

**Title:** `feat: establish sectoral standards adoption governance`

Deliver:

- sector and adoption taxonomies;
- sector-standard mapping model;
- public-services and financial-services illustrative mappings;
- sectoral adoption documentation and validation;
- roadmap and release-evidence integration.

Acceptance criteria:

- sector relevance is not represented as normative adoption;
- every candidate or adopted mapping identifies scope, authority, evidence and review controls;
- mappings resolve to canonical standards-register identifiers;
- illustrative mappings are clearly distinguished from approved sector profiles.

### Commit F — Publish v0.6.0

**Title:** `release: publish v0.6.0 Operational Framework Draft`

Acceptance criteria:

- all release inventories reconcile;
- documentation navigation includes the worked profile and construction tutorial;
- all repository validation passes;
- known limitations accurately state the absence of independent implementation and interoperability evidence.

## 9. v0.6.0 exit gate

The release may be published only when:

- one complete DTF package has been generated through the guided process;
- the sectoral standards-adoption foundation validates and the initial mappings are explicitly marked illustrative;
- the package passes schema, contradiction, completeness, inheritance and traceability checks;
- the operational scenario corpus covers lifecycle, assurance, conformance, rights, risk and maintenance;
- every mandatory core requirement maps to at least one profile provision or justified framework-wide applicability statement;
- the release manifest distinguishes implemented evidence from illustrative material;
- no claim of production conformance, legal adequacy or interoperability is made.

# Part II — v0.7.0 Implementation and Evaluation Draft

## 10. Release objective

`v0.7.0` should establish that independent implementers and assessors can use ONDTF artefacts without relying on unstated knowledge held by the original authors.

The release should answer:

> Can at least one independent implementation be built and evaluated against executable ONDTF assertions, with gaps and ambiguities fed back into the specification?

## 11. v0.7.0 programme structure

The release should be delivered through five work packages.

### WP-7.1 Reference implementation architecture

Build a deliberately minimal reference implementation that demonstrates the operational model without presenting itself as production software.

Suggested components:

- profile loader;
- participant and provider registry;
- status and trust-list service;
- policy decision component;
- evidence evaluator;
- lifecycle controller;
- conformance claim store;
- decision receipt generator;
- challenge and remedy case service;
- audit event stream.

Required architectural properties:

- component boundaries correspond to governed responsibilities;
- identity, authority, admissibility and execution decisions remain separable;
- all decisions produce inspectable records;
- status freshness and cache behaviour are explicit;
- revocation and suspension propagate through defined events;
- affected-party cases are not forced into participant-only models;
- technical choices are isolated in technology bindings.

Deliverables:

```text
reference-implementation/
  README.md
  architecture.md
  components/
  api/
  config/
  fixtures/
  tests/
  deployment/
```

### WP-7.2 Executable conformance suite foundation

Translate the operational scenario corpus into executable assertions.

Test classes:

- positive tests;
- negative tests;
- boundary tests;
- lifecycle tests;
- state-transition tests;
- evidence freshness tests;
- rights and remedy tests;
- profile inheritance tests;
- dependency and version tests;
- security and abuse tests.

Each assertion must include:

- stable test identifier;
- requirement references;
- applicable profile references;
- setup and fixtures;
- execution steps;
- expected result;
- evidence produced;
- severity;
- conformance layer;
- automation status;
- known limitations.

A conformance result format should record:

- implementation under test;
- version and configuration;
- profile and dependency versions;
- test-suite version;
- execution environment;
- test outcomes;
- skipped and not-applicable tests;
- evidence locations;
- assessor identity and competence basis;
- signature or integrity mechanism where profiled.

### WP-7.3 Independent implementation pilot

Recruit or simulate a genuinely independent implementation effort. Independence should mean that the implementer works from published ONDTF documentation and artefacts rather than informal author guidance.

Pilot protocol:

1. publish the implementation brief;
2. freeze a pilot baseline;
3. record questions through a public clarification log;
4. classify each question as documentation gap, specification ambiguity, implementation choice or defect;
5. avoid resolving ambiguity through private channels;
6. run the conformance suite;
7. collect implementation deviations;
8. publish a pilot report;
9. feed accepted findings into normative and explanatory text.

Required evidence:

- implementation diary;
- clarification register;
- failed and passed assertions;
- deviations and rationale;
- time-to-first-successful-scenario;
- documentation discoverability feedback;
- unresolved interoperability assumptions.

### WP-7.4 Jurisdiction and legal-review pilot

Develop one jurisdiction profile through competent review.

Required controls:

- legal cut-off date;
- sources and authority hierarchy;
- reviewer role and competence statement;
- binding, advisory and uncertain classifications;
- explicit unresolved legal questions;
- mapping from legal obligation to ONDTF requirement or profile extension;
- change triggers;
- disclaimer that the profile is not general legal advice.

The aim is not to certify legal compliance. The aim is to validate that ONDTF can carry jurisdiction-specific authority, obligations and uncertainty without corrupting the core.

### WP-7.5 Sector adoption pilots

Run structured pilots for public services and financial services using the v0.6.0 sector-standard mappings. Each pilot should obtain competent sector review, convert illustrative dispositions into candidate decisions, test lifecycle and affected-party coverage, and record conflicts with jurisdictional obligations or established scheme rules.

Required outputs include a sector discovery dossier, capability-and-gap matrix, candidate adoption records, unresolved conflict register, evidence plan and profile-authority decision record.

### WP-7.6 Rights and remedy evaluation pilot

Run structured tabletop or service-design evaluations for affected-party journeys.

Minimum journeys:

- person receives adverse outcome based on incorrect evidence;
- non-participant is harmed by delegated action;
- accessibility barrier prevents digital challenge;
- correction occurs but downstream relying parties retain stale data;
- service provider exits before remedy completes;
- appeal body reverses a supervisory decision;
- emergency suspension causes collateral harm requiring review.

Evaluation dimensions:

- discoverability;
- comprehension;
- timeliness;
- accessibility;
- independence;
- evidence access;
- correction propagation;
- remedy effectiveness;
- auditability;
- risk of retaliation or exclusion.

## 12. v0.7.0 normative refinement tasks

### 12.1 Requirement hardening

For every normative requirement:

- verify one responsible subject;
- define applicability conditions;
- eliminate ambiguous modal language;
- identify measurable evidence;
- distinguish outcome requirement from implementation guidance;
- identify profile-controlled parameters;
- add negative or failure semantics where needed;
- map to one or more tests or explain why it is non-executable.

### 12.2 Terminology refinement

Conduct a term-by-term review for:

- duplicate terms;
- overloaded meanings;
- role versus organisation confusion;
- service versus provider status;
- assurance versus confidence;
- recognition versus technical compatibility;
- conformance versus certification;
- authority versus identity;
- participant versus affected party;
- evidence versus claim;
- suspension, revocation, withdrawal and expiry distinctions.

### 12.3 Implementation-guide layer

Create an implementation guide that explains:

- how to read the core specification;
- how to load a profile;
- how to resolve requirement applicability;
- how to implement lifecycle transitions;
- how to produce decision receipts;
- how to expose status and freshness;
- how to preserve evidence provenance;
- how to implement challenge and remedy workflows;
- how to prepare for conformance testing.

The guide must not create hidden normative obligations.

## 13. v0.7.0 recommended commit sequence

1. `feat: add reference implementation architecture and executable skeleton`
2. `test: establish executable conformance assertion model`
3. `test: implement lifecycle assurance and rights conformance fixtures`
4. `docs: add implementer and assessor guidance`
5. `feat: add competent-review jurisdiction profile pilot`
6. `test: evaluate affected-party challenge and remedy journeys`
7. `docs: incorporate independent implementation findings`
8. `release: publish v0.7.0 Implementation and Evaluation Draft`

## 14. v0.7.0 exit gate

The release may be published only when:

- at least one implementation distinct from the authored examples has been attempted;
- executable tests cover all critical operational paths;
- test results and failures are published;
- at least one jurisdiction profile has documented competent review;
- at least one affected-party journey has been evaluated from notice through remedy;
- implementation questions have been incorporated into documentation or retained as explicit issues;
- requirements without test coverage have a documented reason and review plan;
- URI-03 and URI-04 are either closed with evidence or narrowed with a justified revised target.

# Part III — v0.8.0 Interoperability and Recognition Draft

## 15. Release objective

`v0.8.0` should establish that ONDTF can govern interaction across independent implementations and across trust-framework boundaries.

The release should answer:

> Can two independently developed implementations exchange and evaluate the evidence required by the same profile, and can recognition of an external framework be made explicit, bounded, reversible and testable?

## 16. v0.8.0 work packages

### WP-8.1 Second independent implementation

Develop or recruit a second implementation with meaningful architectural independence.

Independence criteria should include several of the following:

- different codebase;
- different implementation team;
- different language or platform;
- different storage model;
- different selected technology binding;
- different deployment environment;
- no reuse of reference-implementation business logic.

The second implementation should implement the same operational profile and expose the same required externally observable behaviours.

### WP-8.2 Interoperability profile

Create a dedicated interoperability profile defining:

- message and record formats;
- required identifiers and versioning;
- discovery mechanisms;
- status and freshness semantics;
- error taxonomy;
- retry and timeout expectations;
- event propagation;
- evidence integrity;
- capability negotiation;
- cryptographic suite selection;
- privacy and correlation constraints;
- offline and degraded-mode behaviour;
- backwards-compatibility rules.

The profile must distinguish:

- syntactic interoperability;
- semantic interoperability;
- policy interoperability;
- governance interoperability;
- operational interoperability.

Passing one layer must not be represented as passing all layers.

### WP-8.3 Cross-implementation test harness

Create a harness capable of running matrix tests:

| Producer | Consumer | Profile | Scenario | Expected result |
|---|---|---|---|---|
| Implementation A | Implementation B | selected profile | positive | accept |
| Implementation B | Implementation A | selected profile | positive | accept |
| A | B | stale status | negative | reject or constrain |
| B | A | revoked authority | negative | reject |
| A | B | unsupported capability | negotiation | explicit failure |

The harness should test:

- bidirectional exchange;
- inconsistent clock and freshness assumptions;
- partial outages;
- stale caches;
- schema version mismatch;
- unknown issuer or authority;
- suspended provider;
- revoked delegation;
- incomplete evidence;
- rights and remedy reference propagation;
- incident event propagation;
- profile-version mismatch.

### WP-8.4 Interoperability event

Run at least one structured interoperability event.

Event phases:

1. baseline freeze;
2. participant onboarding;
3. environment and endpoint registration;
4. self-test period;
5. blind test execution;
6. adverse-condition execution;
7. issue triage;
8. retest;
9. public results report;
10. specification change proposals.

Publish:

- participant matrix;
- tested versions;
- scenarios run;
- pass, fail and partial results;
- ambiguities encountered;
- defects by implementation versus specification;
- unresolved semantic mismatches;
- remediation status.

### WP-8.5 Recognition profile and equivalence method

Create a governed recognition model that does not equate technical compatibility with legal or institutional recognition.

Recognition profile content:

- recognising authority;
- recognised framework and version;
- legal or policy basis;
- recognised roles and services;
- scope and exclusions;
- assurance equivalence by dimension;
- accepted evidence and trust anchors;
- liability allocation;
- complaints and remedy routing;
- status and incident notification;
- monitoring and periodic review;
- suspension and withdrawal;
- transition and termination;
- unresolved differences.

Equivalence must be multidimensional. A profile should be able to state, for example, that identity evidence is equivalent while remedy, operational supervision or delegated-authority controls are not.

### WP-8.6 Quantitative calibration and operational baselines

Use pilot and test evidence to calibrate selected parameters.

Candidate parameters:

- maximum acceptable status age;
- cache duration;
- revocation propagation objective;
- suspension publication objective;
- incident notification time;
- challenge acknowledgement time;
- correction propagation time;
- appeal resolution objective;
- recovery time and recovery point objectives;
- conformance certificate duration;
- surveillance interval;
- material-change notification window;
- error-rate and availability measures.

Calibration procedure:

1. identify parameter and associated harm;
2. collect evidence from tests, incidents or pilots;
3. document distribution and uncertainty;
4. separate framework minimum from profile default;
5. conduct stakeholder review;
6. record rationale and confidence;
7. define re-calibration trigger.

Where evidence is insufficient, retain the parameter as profile-governed and publish the uncertainty.

### WP-8.7 Cross-sector interoperability and recognition

Use approved sector mappings to test whether standards selected by different sector profiles produce compatible evidence, status, authority and remedy semantics. Record where common technical standards conceal different sector policy, assurance or legal effects.

### WP-8.8 Adversarial and resilience exercises

Run adversarial exercises covering:

- collusion between provider and assessor;
- compromised registry operator;
- delayed suspension propagation;
- authentic but invalidly exercised authority;
- malicious profile downgrade;
- recognition of an external framework with weaker remedy;
- dependency compromise;
- status-query correlation attack;
- evidence replay;
- denial of challenge access;
- selective incident disclosure;
- provider exit during active disputes.

Outputs:

- attack narrative;
- affected assets and parties;
- failed assumptions;
- observable signals;
- required controls;
- residual risk;
- specification changes;
- test additions.

## 17. v0.8.0 documentation and learning requirements

Add guided learning routes for:

- interoperability implementers;
- recognition authorities;
- profile comparison reviewers;
- test-event participants;
- assurance-calibration reviewers.

Add diagrams for:

- capability negotiation;
- status and revocation propagation;
- recognition decision lifecycle;
- assurance equivalence comparison;
- cross-framework complaint and remedy routing;
- interoperability event workflow;
- profile-version migration.

Every diagram must have adjacent explanatory prose and an accessible text equivalent where necessary.

## 18. v0.8.0 recommended commit sequence

1. `feat: define the ONDTF interoperability profile`
2. `feat: add a second independent profile implementation`
3. `test: add cross-implementation interoperability harness`
4. `test: run and document the first interoperability event`
5. `feat: establish recognition profiles and assurance equivalence`
6. `test: add adversarial interoperability and recognition scenarios`
7. `docs: calibrate operational parameters from pilot evidence`
8. `docs: integrate interoperability and recognition learning paths`
9. `release: publish v0.8.0 Interoperability and Recognition Draft`

## 19. v0.8.0 exit gate

The release may be published only when:

- at least two independent implementations have completed a documented interoperability matrix;
- bidirectional positive and negative tests have been run;
- semantic mismatches and failures are published rather than hidden;
- one complete recognition profile has been evaluated;
- assurance equivalence is represented dimension by dimension;
- recognition suspension and withdrawal are tested;
- selected operational parameters have evidence-backed defaults or explicit uncertainty;
- adversarial exercises have produced specification or test-suite changes;
- URI-01, URI-02, URI-13, URI-14 and URI-16 are closed, narrowed or formally deferred with evidence.

# Part IV — v0.9.0 Candidate Specification

## 20. Release objective

`v0.9.0` should freeze the candidate normative architecture for final review and implementation feedback.

The release should answer:

> Is the ONDTF normative core complete, internally consistent, independently implementable, interoperable under selected profiles, governed through stable change control, and suitable for candidate-specification review?

Candidate status should not mean that no defects remain. It should mean that:

- the normative surface is known;
- requirements are stable enough for independent review;
- changes are controlled;
- conformance targets are explicit;
- implementation and interoperability evidence exists;
- unresolved issues are bounded and visible;
- release criteria for v1.0.0 are defined.

## 21. Candidate-specification preparation work packages

### WP-9.1 Normative text freeze and editorial consolidation

Conduct a complete specification review.

Tasks:

- identify every normative document;
- eliminate duplicate requirements;
- ensure every requirement has a stable identifier;
- resolve conflicting obligations;
- verify modal verb usage;
- separate rationale, examples and implementation guidance from requirements;
- define applicability and exceptions;
- eliminate internal planning language;
- ensure terminology is consistent across human and machine-readable artefacts;
- freeze section anchors and stable references;
- identify all profile extension points;
- define deprecation policy for normative identifiers.

Produce a normative-document manifest classifying each artefact as:

- core normative;
- profile normative;
- conformance normative;
- informative guidance;
- example;
- implementation evidence;
- governance process.

### WP-9.2 Requirements coverage and traceability closure

For every normative requirement, require links to:

- source rationale or decision;
- responsible subject;
- applicability conditions;
- profile parameters;
- evidence expectation;
- one or more conformance assertions, or a documented reason for non-executable assessment;
- implementation evidence where applicable;
- risk or harm addressed;
- change history.

Generate coverage reports for:

- requirements without tests;
- tests without requirements;
- requirements without accountable roles;
- profile provisions without core source or extension authority;
- generated sections without construction decisions;
- issues without closure evidence;
- terms used but not defined.

Candidate release must have zero unexplained critical gaps.

### WP-9.3 Terminology validation and semantic review

Create a formal terminology-validation process.

Activities:

- glossary consistency linting;
- defined-term capitalization and linking;
- external terminology crosswalks;
- role and state-name validation;
- review by implementers, governance practitioners and rights specialists;
- identification of terms likely to be misread across jurisdictions;
- controlled aliases where necessary;
- explicit non-equivalences.

High-priority terms include:

- authority;
- assurance;
- accreditation;
- assessment;
- certification;
- conformance;
- recognition;
- equivalence;
- trust service;
- trust framework;
- profile;
- participant;
- affected party;
- provider;
- relying party;
- status;
- suspension;
- revocation;
- withdrawal;
- delegation;
- admissibility;
- remedy.

### WP-9.4 Candidate conformance suite

Promote the conformance suite from a foundation into a candidate suite.

Requirements:

- stable test identifiers;
- versioned test profiles;
- positive, negative, boundary and adversarial coverage;
- machine-readable result format;
- implementation configuration disclosure;
- deterministic fixtures where feasible;
- clear handling of optional and profile-dependent requirements;
- assessor guidance;
- evidence retention expectations;
- suite self-tests;
- published coverage statistics.

Define candidate conformance classes, for example:

- Core Governance Conformance;
- Operational Profile Conformance;
- Technology Profile Conformance;
- Rights and Remedy Conformance;
- Interoperability Profile Conformance;
- Recognition Profile Conformance.

No generic claim of “ONDTF compliant” should be allowed without naming the applicable conformance class, profile, version and assessment basis.

### WP-9.5 Independent review programme

Run structured review rounds.

Reviewer groups:

- implementers;
- trust-framework operators;
- regulators or public authorities;
- conformity-assessment specialists;
- privacy and security experts;
- accessibility and rights specialists;
- legal and jurisdiction-profile reviewers;
- interoperability participants;
- affected-party or civil-society representatives.

Review protocol:

1. publish review package and scope;
2. assign stable review-comment identifiers;
3. classify comments as editorial, technical, governance, rights, security, interoperability or blocking;
4. record disposition and rationale;
5. identify changes requiring renewed implementation testing;
6. publish comment-resolution report;
7. rerun impacted validations;
8. obtain final editorial and release approval.

### WP-9.6 Controlled change and maintenance readiness

Activate candidate-level governance.

Required mechanisms:

- normative change proposal template;
- change impact assessment;
- backwards-compatibility classification;
- security emergency process;
- profile update and migration rules;
- dependency-watch process;
- deprecation schedule;
- issue severity model;
- release branch policy;
- errata process;
- candidate review window;
- v1.0.0 entrance criteria.

Any normative change after candidate freeze should require:

- identified problem;
- affected requirements and profiles;
- implementation impact;
- conformance impact;
- migration plan;
- review and approval record;
- updated evidence.

### WP-9.7 Guided construction candidate hardening

The Guided Framework Construction capability must itself reach candidate quality.

Tasks:

- complete question coverage across all normative domains;
- eliminate duplicate or ambiguous questions;
- ensure every question maps to one or more generated artefacts;
- ensure every generated normative decision maps back to a question, inherited default or profile rule;
- add question-set versioning and migration;
- add response-set validation and provenance;
- add deterministic generation tests;
- add redaction and publication controls;
- support workshop and asynchronous modes;
- support partial saves and unresolved decisions;
- produce a completeness and review dashboard;
- validate at least two independently constructed DTF packages.

The guided flow should explicitly refuse to convert political, legal or stakeholder judgement into automatic defaults where authority or legitimacy requires external evidence.

### WP-9.8 Sectoral register candidate governance

Promote the sectoral standards layer to candidate quality by completing taxonomy governance, mapping provenance, review ownership, dependency monitoring, supersession and retirement rules, normative-claim linting, and at least two independently reviewed sector profiles.

### WP-9.9 Documentation architecture candidate review

Perform a complete information-architecture audit.

Audit dimensions:

- first-time reader orientation;
- role-based entry points;
- specification versus guidance separation;
- navigation completeness;
- previous/next integrity;
- orphan-page detection;
- duplicate-content detection;
- diagram rendering;
- heading hierarchy;
- accessible link text;
- glossary linkage;
- canonical URLs;
- version banners;
- stale-document warnings;
- release-specific documentation views;
- mobile and narrow-screen usability;
- print and PDF suitability where supported.

Create role-specific “start here” routes for:

- framework authority;
- profile author;
- implementer;
- provider;
- assessor;
- relying party;
- rights and remedy operator;
- interoperability participant;
- reviewer.

## 22. v0.9.0 recommended commit sequence

A granular but reviewable candidate path would use the following commits.

### Commit 9A — Normative inventory and freeze preparation

**Title:** `docs: establish candidate normative inventory and freeze controls`

Deliver:

- normative artefact classification;
- freeze policy;
- stable requirement and section inventory;
- known duplicate and conflict report.

### Commit 9B — Requirements and terminology consolidation

**Title:** `refactor: consolidate normative requirements and terminology`

Deliver:

- deduplicated requirements;
- terminology corrections;
- applicability clarifications;
- profile extension-point definitions;
- updated schemas and cross-references.

### Commit 9C — Candidate conformance suite

**Title:** `test: promote the conformance suite to candidate coverage`

Deliver:

- stable assertions;
- coverage matrix;
- result schemas;
- conformance classes;
- suite self-tests.

### Commit 9D — Guided construction hardening

**Title:** `feat: harden guided framework construction for candidate use`

Deliver:

- full question coverage;
- response migration;
- deterministic generation;
- completeness dashboard;
- second generated DTF package.

### Commit 9E — Independent review package

**Title:** `docs: publish the candidate review package and review protocol`

Deliver:

- reviewer guidance;
- comment template;
- review matrix;
- review build or snapshot;
- issue classification rules.

### Commit 9F — Resolve candidate review findings

**Title:** `fix: resolve candidate review and implementation findings`

Deliver:

- disposition report;
- accepted normative changes;
- updated tests;
- rerun interoperability evidence where affected;
- residual issue register.

### Commit 9G — Candidate governance and maintenance

**Title:** `governance: activate candidate change and maintenance controls`

Deliver:

- errata process;
- emergency change process;
- dependency monitoring;
- release-branch policy;
- v1.0.0 entrance criteria.

### Commit 9H — Documentation architecture audit

**Title:** `docs: complete candidate documentation and learning architecture audit`

Deliver:

- corrected navigation;
- role-based paths;
- version banners;
- accessibility improvements;
- diagram and link audit;
- stale-page detection.

### Commit 9I — Publish v0.9.0

**Title:** `release: publish v0.9.0 Candidate Specification`

Deliver:

- release notes;
- release manifest;
- normative inventory;
- evidence inventory;
- test coverage report;
- implementation and interoperability report;
- review disposition report;
- known limitations;
- v1.0.0 readiness plan.

## 23. v0.9.0 candidate exit gate

`v0.9.0` may be published only when all of the following are true.

### Normative completeness

- every normative requirement has a stable identifier;
- no unresolved normative conflicts remain;
- requirement subjects and applicability are explicit;
- mandatory, recommended, optional and profile-controlled provisions are distinguishable;
- normative and informative content are clearly separated.

### Traceability

- every normative requirement maps to evidence and conformance expectations;
- every executable test maps to one or more requirements;
- every generated profile decision maps to a construction source;
- every profile provision has a permitted relationship to the core;
- critical issues include closure evidence.

### Implementation

- at least two implementations exist;
- at least one was developed independently from the reference implementation logic;
- implementation deviations and unresolved questions are published;
- the worked operational profile remains executable after candidate changes.

### Interoperability

- bidirectional tests have been completed;
- positive, negative and mismatch cases have been run;
- status, revocation, freshness and profile-version behaviour are tested;
- unresolved semantic mismatches are explicitly documented.

### Conformance

- the candidate suite has stable identifiers and result formats;
- critical requirements have executable or assessor-verifiable checks;
- conformance classes and claim language are defined;
- no unqualified “ONDTF compliant” claim is permitted.

### Rights and remedy

- affected-party journeys have been evaluated;
- challenge, correction, appeal and remedy records are testable;
- accessibility and alternative channels are represented;
- correction and remedy propagation are addressed.

### Governance

- candidate change controls are active;
- controlled-document ownership is complete;
- dependency monitoring and emergency-change procedures are documented;
- review comments and dispositions are published;
- remaining issues are bounded and assigned.

### Documentation

- all published pages are discoverable;
- role-based learning paths are complete;
- previous/next navigation is valid;
- diagrams render;
- terminology is linked and consistent;
- no internal-only planning terms remain;
- version and status labels are accurate.

# Part V — Cross-release controls

## 24. Master dependency chain

```text
Current governed profile and construction baseline
    ↓
Generated worked operational DTF
    ↓
Operational scenario and traceability corpus
    ↓
v0.6.0 Operational Framework Draft
    ↓
Reference implementation and executable conformance foundation
    ↓
Independent implementation, legal-profile and remedy pilots
    ↓
v0.7.0 Implementation and Evaluation Draft
    ↓
Second independent implementation and interoperability profile
    ↓
Cross-implementation event, recognition and calibration evidence
    ↓
v0.8.0 Interoperability and Recognition Draft
    ↓
Normative freeze, candidate conformance and independent review
    ↓
v0.9.0 Candidate Specification
```

## 25. Issue closure plan

The maturation register should be updated at every release, but issues should close only against evidence.

| Issue | Expected closure target | Minimum closure evidence |
|---|---|---|
| URI-01 Multi-implementation evidence | v0.8.0 | two independent implementations and cross-test report |
| URI-02 Quantitative calibration | v0.8.0 | pilot data, confidence ranges and reviewed defaults or explicit uncertainty |
| URI-03 Jurisdiction legal review | v0.7.0 | competent review, cut-off date and unresolved-question register |
| URI-04 Complete conformance suite | v0.7.0 or narrowed at v0.7.0 | executable positive, negative, boundary and lifecycle assertions |
| URI-05 Privacy-preserving status comparison | v0.7.0 | comparative analysis and leakage/freshness tests |
| URI-06 Rights and accessibility validation | v0.7.0–v0.8.0 | evaluated affected-party journeys and accessibility evidence |
| URI-07 Standards maintenance | v0.9.0 ongoing control | active dependency register and change-impact process |
| URI-08 Role obligations | v0.6.0 | complete normative catalogue mapped to roles |
| URI-09 Accreditation model | v0.6.0, validated v0.7.0 | assessment scheme plus pilot evidence |
| URI-10 Provider lifecycle | v0.6.0 | complete state model and scenario coverage |
| URI-11 Institutional governance | v0.6.0 | worked governance model and decision matrix |
| URI-12 Profile construction | v0.6.0 | generator and validated worked profile |
| URI-13 Performance baselines | v0.8.0 | measured baselines and uncertainty |
| URI-14 Adversarial exercises | v0.8.0 | published exercises and resulting changes |
| URI-15 Terminology validation | v0.9.0 | formal terminology review and linting |
| URI-16 Assurance equivalence | v0.8.0 | dimension-by-dimension recognition profile |
| URI-17 Challenge and remedy pilots | v0.7.0–v0.8.0 | end-to-end pilot evidence |
| URI-18 Maintenance model | v0.9.0 | candidate change, errata and dependency controls |
| URI-19 External pattern adoption | v0.8.0–v0.9.0 | adopted-pattern register with evidence and maintenance owners |

## 26. CI and validation evolution

### By v0.6.0

CI should validate:

- generated package completeness;
- construction-response schemas;
- contradiction and completeness gates;
- profile inheritance;
- requirement and role references;
- documentation navigation;
- YAML, JSON and Mermaid syntax.

### By v0.7.0

Add:

- reference implementation tests;
- conformance assertion execution;
- fixture validation;
- API contract tests;
- deterministic generation tests;
- rights and remedy workflow tests;
- coverage reports.

### By v0.8.0

Add:

- cross-implementation harness execution;
- interoperability matrix reports;
- profile-version compatibility tests;
- status and revocation propagation tests;
- recognition-profile validation;
- quantitative-baseline checks.

### By v0.9.0

Add:

- normative coverage gates;
- undefined-term and duplicate-requirement checks;
- candidate identifier stability checks;
- normative-versus-informative classification checks;
- conformance class validation;
- release evidence reconciliation;
- candidate branch and version controls.

## 27. Documentation architecture controls

Every substantive addition must satisfy the following documentation-definition-of-done.

- Page has a clear purpose and intended audience.
- Page states whether it is normative, informative, generated or evidentiary.
- Page is included in the relevant landing page.
- Page appears in the site map and canonical reading order where appropriate.
- Previous and next links are valid.
- Related machine-readable artefacts are linked.
- Related requirements, roles, profiles and evidence are linked.
- Diagrams have explanatory prose.
- No section depends on an unexplained acronym.
- Examples are marked as examples and do not create hidden requirements.
- Version-sensitive content has a review date or dependency reference.
- Internal delivery labels and temporary planning terminology do not appear in published content.

## 28. Evidence inventory model

Introduce a canonical evidence inventory with fields such as:

```yaml
id: EVD-0001
title: Provider suspension propagation test
class: interoperability
release: v0.8.0
status: accepted
source:
  type: test-run
  location: evidence/interoperability/event-01/results.json
supports:
  requirements:
    - ONDTF-OPS-...
  issues:
    - URI-01
    - URI-13
  release_gates:
    - RG-v0.8.0
review:
  reviewers:
    - role: Interoperability Workstream
  reviewed_at: 2026-...
limitations:
  - Tested only under selected technology profile
```

Evidence should be classified as:

- design;
- implementation;
- conformance;
- interoperability;
- operational;
- assurance;
- rights;
- recognition;
- governance;
- review.

## 29. Risk controls for the roadmap

### Risk: excessive scope growth

Control:

- require every new capability to map to a release gate or open issue;
- reject unrelated feature additions before v0.9.0;
- prefer evidence and refinement over new conceptual domains.

### Risk: reference implementation becomes de facto normative

Control:

- label it non-normative;
- maintain at least one independent implementation;
- keep technology choices in profiles and bindings;
- test observable behaviour rather than internal architecture.

### Risk: guided construction creates false confidence

Control:

- preserve unresolved decisions;
- require authority, legal, stakeholder and expert review evidence;
- show inherited defaults explicitly;
- prevent automatic completion where legitimacy cannot be inferred.

### Risk: conformance suite overclaims governance quality

Control:

- distinguish machine-testable, assessor-verifiable and judgement-dependent requirements;
- require named conformance classes;
- retain evidence and assessor competence records;
- prohibit generic compliance claims.

### Risk: interoperability reduced to message exchange

Control:

- test semantic, policy, governance and operational interoperability separately;
- include rights, incident and recognition paths;
- publish partial passes honestly.

### Risk: candidate freeze occurs before sufficient review

Control:

- require independent review evidence;
- set minimum review windows;
- reopen candidate tests after material normative changes;
- defer candidate status rather than waive critical gates.

## 30. Release management cadence

A practical cadence could use the following sequence for each release:

1. scope freeze;
2. work-package implementation;
3. internal integration review;
4. evidence capture;
5. public or independent review;
6. issue disposition;
7. release-candidate branch;
8. full validation;
9. release approval;
10. publication and post-release issue triage.

Each release should have a named release steward and separate approval roles for:

- specification content;
- conformance evidence;
- documentation quality;
- governance and issue closure;
- release integrity.

## 31. Definition of done by release

### v0.6.0 done means

A complete DTF can be generated, validated and understood.

### v0.7.0 done means

An independent implementer can build and assess it, and practical gaps have been incorporated.

### v0.8.0 done means

Two implementations can interoperate under a governed profile, and recognition can be bounded and reversed.

### v0.9.0 done means

The normative core is stable, traceable, independently reviewed and governed as a candidate specification.

## 32. Recommended immediate next action

The immediate next delivery should be the worked operational profile and its complete guided-construction response set. This is the highest-leverage step because it creates the input needed for:

- the generator;
- operational scenarios;
- conformance assertions;
- the reference implementation;
- the independent implementation brief;
- the interoperability profile;
- candidate traceability.

In parallel, establish the sectoral standards-adoption foundation so later pilots inherit stable taxonomies, mapping semantics and decision controls. The first pre-release milestone should therefore be:

> Produce one complete, reviewable decision set for a representative national digital trust service and prove that every decision can be transformed into a governed DTF artefact without hidden manual assumptions.

## 33. Summary roadmap

| Release | Primary deliverable | Evidence threshold |
|---|---|---|
| v0.6.0 | Generated worked DTF, operational scenario corpus and sectoral adoption foundation | internal consistency, complete traceability and governed sector mapping |
| v0.7.0 | Reference implementation, executable conformance and independent pilot | independent implementability and evaluation |
| v0.8.0 | two implementations, interoperability event and recognition profile | cross-implementation and cross-framework evidence |
| v0.9.0 | frozen normative core, candidate conformance and independent review | candidate stability, traceability and controlled change |

The roadmap deliberately makes `v0.9.0` the outcome of accumulated evidence rather than accumulated prose. If followed, ONDTF should arrive at candidate status with a defensible chain from governance decision to requirement, implementation, conformance evidence, interoperability result, review disposition and controlled release.
