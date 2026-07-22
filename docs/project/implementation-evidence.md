---
layout: default
title: Implementation Evidence Programme
parent: Project Governance and Releases
nav_order: 15
---

# Implementation evidence programme

## Objective

The programme converts ONDTF from an architecturally complete draft into an implementation-informed specification. It should accumulate evidence without treating one reference stack as the framework itself.

## Evidence classes

| Class | Examples | Claim supported |
|---|---|---|
| Design evidence | Architecture review, threat analysis, profile mapping | A requirement or pattern is coherent and traceable. |
| Implementation evidence | Independent code, configuration, deployment record | A requirement can be implemented outside the reference artefacts. |
| Conformance evidence | Positive, negative and lifecycle tests | An implementation satisfies a named profile and version. |
| Operational evidence | Metrics, incidents, recovery exercises, status propagation | The implementation behaves acceptably under realistic conditions. |
| Rights evidence | Notice, challenge, accessibility, appeal and remedy journeys | Affected parties can understand, contest and obtain remedy. |
| Recognition evidence | Equivalence assessment, legal basis, status and dispute rules | Reliance across frameworks is bounded and governed. |

## Minimum evidence path

- **v0.6.0:** one complete implementation profile and pilot kit;
- **v0.7.0:** at least one independent implementation and executable baseline suite;
- **v0.8.0:** at least two implementations participating in cross-implementation tests;
- **v0.9.0:** independently reviewable evidence supporting the Candidate Specification gate.

Evidence must identify the ONDTF version, selected profile, implementation version, test environment, limitations, failures and responsible evaluator. Unqualified claims such as “ONDTF compliant” are not acceptable.
