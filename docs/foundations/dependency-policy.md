---
layout: default
title: Reference and Dependency Policy
parent: Foundations
nav_order: 5
---
# Reference and Dependency Policy

ONDTF distinguishes a **reference** from a **normative dependency**. Referencing an external model, schema, protocol, or implementation does not make it mandatory for core adoption.

## Core rule

Core ONDTF conformance shall not require use of a particular meta-model, schema language, protocol suite, registry implementation, or software stack. A named jurisdiction, sector, or technical profile may impose a specific dependency where necessary for that profile's interoperability objective.

## Optional references

An optional reference records:

- source and version reviewed;
- purpose of the crosswalk or compatibility statement;
- known semantic differences;
- equivalent ONDTF capabilities;
- whether any named profile selects it.

## Normative profile dependencies

Where a profile creates a normative dependency, it must record:

- exact specification or immutable reference;
- required capability and rationale;
- compatibility range;
- failure behaviour when unavailable or incompatible;
- migration and deprecation policy;
- accountable profile authority.

ONDTF shall not silently inherit changes from a moving external branch. Alternative implementations remain permissible unless the declared profile explicitly and justifiably restricts them.
