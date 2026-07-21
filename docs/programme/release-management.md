---
layout: default
title: Release Management
parent: Programme Management
nav_order: 6
---

# Release management

ONDTF distinguishes ordinary repository changes from releases that establish a new reference point for adopters, reviewers, profiles, or implementations.

## Commit-only threshold

A change normally requires a commit but not a release when it:

- corrects spelling, broken links, navigation, or formatting;
- fixes GitHub Pages, CI, or Mermaid rendering without changing normative meaning;
- clarifies existing text without altering obligations, scope, or conformance;
- improves diagrams while preserving the represented architecture;
- adds internal delivery artefacts that downstream users do not need to cite;
- refreshes examples or references without changing the applicable profile.

Such commits should update the changelog only when the change is externally material.

## Patch release threshold

A patch release is appropriate when a correction is externally relevant but backward compatible, including:

- correction of an ambiguity that could lead to materially different implementation;
- repair of a published artefact or profile required by adopters;
- security or privacy clarification that does not change the declared feature set;
- conformance-test correction that preserves the normative requirement.

## Minor release threshold

A minor release is required when the repository introduces a new substantive baseline, including:

- a new normative requirement family;
- a new conformance class or profile method;
- a new architecture or operating-model domain intended for adoption;
- a machine-readable artefact intended for external implementation;
- a material change to scope, terminology, lifecycle, governance, or assurance;
- a publication milestone that downstream work will cite.

## Candidate and stable releases

A candidate release requires completed scope, public review evidence, conformance coverage, and documented limitations. A stable release additionally requires approved governance, implementation evidence, migration guidance, and controlled change management.

## Decision for v0.3.0

The core specification and target operating model constitute a new normative and institutional baseline. They are intended to be cited by later architecture, profile, assurance, and conformance work. The payload therefore warrants a minor release rather than a commit-only treatment.
