---
layout: default
title: Specification Maturity and Evidence Governance
parent: Project Governance and Releases
nav_order: 18
---
# Specification Maturity and Evidence Governance

## Purpose

ONDTF separates **specification maturity** from **implementation evidence maturity** so that the framework can continue to improve without converting absence of externally controlled evidence into either a false pass or an indefinite release veto.

The governing principle is claim-scoped evidence: evidence is mandatory for the claim it supports, but evidence whose production is exclusively controlled by an external actor does not block unrelated specification maintenance or maturation.

> No release shall require evidence whose production is exclusively dependent upon an external actor unless the absence of that evidence prevents the specific claim made by the release. External evidence may constrain an assurance, conformance, interoperability, deployment, or validation claim; it SHALL NOT indefinitely prevent maintenance or maturation of the specification itself.

The machine-readable authority for the current maturity state is [`governance/maturity.yaml`](../../governance/maturity.yaml).

## 1. Specification maturity

ONDTF uses three specification states:

| State | Meaning |
|---|---|
| `draft` | The normative surface may change materially and consumers should expect instability. |
| `candidate` | The normative surface is controlled, traceable and reviewable, but final stability gates remain open. |
| `stable` | The normative contract is governed as a dependable baseline with controlled compatibility and change semantics. |

A stable specification is a claim about the quality and governance of the specification itself. It is not a claim of production readiness, legal approval, independent implementation validation or externally demonstrated interoperability.

## 2. Evidence maturity

Evidence maturity evolves independently and is version-scoped.

| Level | Evidence claim |
|---|---|
| `E0` | Specification evidence only. |
| `E1` | Repository-controlled reference implementation or executable evidence exists. |
| `E2` | Independent implementation evidence exists. |
| `E3` | Cross-implementation interoperability evidence exists. |
| `E4` | Operational deployment evidence exists. |

Evidence levels are cumulative only when their underlying evidence remains current and applicable to the ONDTF version and profile under claim.

## 3. Claim boundaries

A release MUST state both its specification maturity and its external evidence state.

The following claims require corresponding evidence and MUST NOT be inferred from a stable specification version alone:

- independently validated implementation;
- externally demonstrated interoperability;
- operational deployment validation;
- production readiness;
- competent legal or regulatory approval.

Missing evidence remains `missing`; repository-controlled evidence MUST NOT be reclassified as independent evidence merely to satisfy a promotion criterion.

## 4. v1.0.0 promotion rule

Promotion to `v1.0.0` establishes a **stable ONDTF specification baseline**.

The promotion gate is satisfied through repository-controlled evidence demonstrating, at minimum:

- stable normative identifiers and terminology;
- complete requirement-to-conformance traceability;
- deterministic repository validation;
- negative and adversarial evidence for consequential requirements;
- explicit compatibility and normative-change controls;
- an active errata and emergency-change process;
- disposition of internally controllable blocking issues;
- reproducible release integrity;
- explicit declaration of current external evidence maturity.

Independent implementation is required for an `E2` or independently validated implementation claim. It is not required merely to continue ONDTF specification maturation or to establish specification stability.

## 5. Evidence invalidation and revocation

Evidence maturity is not permanent. Evidence MUST be reassessed when any of the following occurs:

- a material normative change affects the proposition previously tested;
- evidence expires or exceeds its governed freshness period;
- an evidence source is withdrawn or shown to be unreliable;
- the implementation that generated the evidence is superseded in a material way;
- a defect is discovered that falsifies a previously accepted claim.

An invalidating event may reduce the evidence level for a specific version, profile, capability or claim without changing the specification maturity state unless the event also demonstrates a specification defect.

## 6. Independent implementability without implementation theatre

ONDTF should continue to pressure-test whether an implementer can interpret and apply the framework without undocumented maintainer knowledge. Useful repository-controlled falsification channels include:

- clean-room implementation from published normative artefacts only;
- independently authored profile construction exercises;
- alternative technology bindings;
- semantic ambiguity and adversarial interpretation tests;
- machine-generated conformance vectors;
- deliberately incomplete or hostile implementation fixtures;
- external expert review of normative clarity and testability.

These activities can strengthen the specification and may support `E1`. They do not substitute for `E2` independent implementation evidence.

## 7. Authority and delegation

ONDTF controls specification authority, release governance and repository evidence. External implementers, operators, assessors and reviewers control the evidence they generate.

The framework therefore delegates no veto over specification evolution to external actors. External actors instead determine whether stronger implementation, interoperability or operational evidence claims can be made.

## 8. Release reporting

Each future release should report:

- specification maturity;
- evidence level;
- newly added evidence;
- invalidated or superseded evidence;
- claims permitted by the evidence state;
- claims explicitly not made;
- material changes that require reassessment.

This keeps maturity, assurance and adoption evidence visible without conflating them.
