---
title: TIS Artefact Adoption
parent: Foundations
nav_order: 6
---
# TIS Compatibility Profile

[TIS v0.12.0](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) provides an optional compatible suite of machine-readable artefacts. ONDTF core does not require TIS. A named profile may select or constrain TIS where that choice serves an explicit interoperability need.

| TIS artefact family | ONDTF baseline treatment | Intended use |
|---|---|---|
| Authority boundary | Required for assured authority decisions | Identify controlling authority, scope, exclusions, and accountability boundary |
| Delegation lineage | Required where authority is derived | Preserve parent authority, attenuation, expiry, and revocation lineage |
| Evidence-bundle manifest | Required for high-impact decisions | Bind evidence items, integrity data, provenance, and evaluation context |
| Decision receipt | Required for reviewable consequential effects | Record decision, policy, authority, evidence, reason, and admitted effect |
| Registry entry | Required for recognised trust services and authorities | Publish identifiers, status, scope, endpoints, and assurance metadata |
| Registry publication profile | Required for federated publication | Define publication, discovery, update, and withdrawal expectations |
| Status and revocation evidence | Required where lifecycle state affects reliance | Provide freshness and status semantics |
| Conformance declaration | Required for formal ONDTF claims | State profile, version, tested capabilities, and limitations |
| Assurance level | Required where a profile defines tiered reliance | Express assurance dimensions without collapsing them to one score |
| Runtime governance projection | Recommended for dynamic systems and agents | Carry bounded runtime policy and authority context |
| Trust-task lifecycle evidence | Required for delegated high-impact tasks | Record initiation, execution, checkpoints, completion, and failure |

## Composition rule

A profile that selects TIS may constrain an artefact by making optional properties mandatory, narrowing enumerations, setting freshness requirements, or requiring linked artefacts. Such a profile must identify its TIS version and must not silently change TIS semantics.
