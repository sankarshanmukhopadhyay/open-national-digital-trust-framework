---
layout: default
title: Profile Requirement Inheritance
parent: Normative Architecture
nav_order: 3
---

# Profile requirement inheritance

Profiles are the controlled mechanism through which ONDTF is adapted to a jurisdiction, sector, trust service or technology environment.

## Precedence model

The applicable obligation set is composed in this order:

1. ONDTF core requirements;
2. jurisdiction profile requirements;
3. sector or trust-scheme profile requirements;
4. technology profile requirements;
5. approved local controls and procedures.

A lower layer may strengthen, specialise or operationalise a higher-layer requirement. It must not silently weaken or remove it.

## Permitted profile actions

A profile may:

- add requirements;
- convert a core `SHOULD` into a profile `MUST`;
- define thresholds, time limits and evidence formats;
- select external standards and versions;
- allocate responsibilities to named institutions;
- constrain permitted technologies;
- introduce stronger rights, privacy, security or resilience obligations.

A profile may not:

- turn a core `MUST` into a recommendation;
- remove an affected-party protection without an authorised framework-level change;
- substitute authentication for authority evaluation;
- claim legal recognition not established by competent authority;
- conceal extensions, deviations or dependencies.

## Conflict handling

A profile must record every apparent conflict with a core requirement. The profile authority must resolve the conflict by:

- demonstrating that the profile is a compatible specialisation;
- changing the profile;
- proposing a controlled ONDTF amendment; or
- recording that the profile cannot claim ONDTF conformance.

## External dependencies

When a profile selects an external specification, it must declare:

- canonical title and owner;
- exact version or edition;
- normative status within the profile;
- selected clauses or features;
- local constraints or extensions;
- maintenance and migration responsibility;
- effects of withdrawal or incompatibility.
