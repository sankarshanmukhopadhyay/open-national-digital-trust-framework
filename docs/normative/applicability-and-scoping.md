---
layout: default
title: Applicability and Scoping
parent: Normative Architecture
nav_order: 2
---

# Applicability and scoping

A requirement is meaningful only when the object, role, interaction and effect to which it applies are explicit.

## Applicability classes

| Class | Applies to |
|---|---|
| core | Every adoption claiming ONDTF core conformance |
| institutional | Bodies exercising governance, supervision, assessment, review or operational authority |
| scheme | A governed trust scheme and its scheme authority |
| provider | An admitted provider or operator |
| service | A service placed within an ONDTF profile or scheme |
| implementation | Software, infrastructure or technical components |
| interaction | A defined transaction, decision or effect |
| affected-party | Processes through which people or organisations receive notice, challenge or remedy |
| profile | The profile authority and the profile specification itself |

A requirement may declare more than one class, but its catalogue entry must identify the primary assessed object.

## Conformance scope statement

Every conformance claim must state:

1. the ONDTF version;
2. the adopted profile and version, if any;
3. the assessed object and organisational boundary;
4. the roles performed by the claimant;
5. included and excluded services;
6. applicable requirement identifiers;
7. approved exceptions;
8. evidence cut-off date;
9. validity period.

A claim must not imply conformance outside that scope.

## Conditional applicability

A conditional requirement uses a machine-readable `condition` and must identify the event or design choice that activates it. Examples include operating a shared registry, permitting re-delegation, making an automated adverse decision or processing sensitive personal information.

The absence of a selected technology does not remove an outcome requirement. A profile selecting a technical mechanism must show how it satisfies the relevant outcome and evidence obligations.

## Multiple roles

One institution may perform multiple roles where law and profile governance permit it. The institution must then:

- declare each role separately;
- apply every requirement associated with each role;
- assess concentration and conflict risks;
- implement compensating safeguards;
- preserve independent review where consequences are material.

Combining roles does not collapse their obligations into one undifferentiated responsibility.
