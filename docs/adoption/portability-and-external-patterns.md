---
layout: default
title: Portability and External Patterns
parent: Adoption
nav_order: 9
---
# Portability and external patterns

ONDTF defines governance outcomes and transferable patterns before an adopter selects protocols, schemas, registries, credentials, proof mechanisms, or implementation stacks. This preserves portability across jurisdictions, sectors and technical ecosystems.

## Portability invariant

> An external ecosystem may implement, specialise or constrain an ONDTF capability through a governed profile, but it does not define the ONDTF core requirement itself.

A reader must therefore be able to remove every external example from ONDTF documentation and still retain a complete, interpretable normative core.

## Capability before mechanism

The adoption sequence is:

```mermaid
flowchart LR
  N[Governance need] --> C[Required capability]
  C --> O[Required outcomes]
  O --> P[ONDTF pattern]
  P --> M[External mechanism selection]
  M --> S[Substitutability / exclusivity decision]
  S --> E[Evidence and conformance]
```

This is why GFC-TEC-001 now requires the adopter to identify required capabilities and outcomes before recording concrete dependencies.

## Portability principles

1. **Core independence.** Core requirements remain interpretable without any external ecosystem.
2. **Capability before mechanism.** Technology selection follows the governance capability and required outcomes.
3. **No privileged ecosystem.** No external ecosystem receives structural or normative preference in the core.
4. **Explicit normative effect.** Adoption records state whether an external pattern is informative or profile-normative.
5. **Substitutability.** Where multiple mechanisms can satisfy the same outcome, the profile records that alternatives are permitted.
6. **Non-weakening.** External adoption may specialise or strengthen ONDTF obligations but cannot silently weaken mandatory requirements.
7. **Change isolation.** External version changes trigger dependency/profile review rather than implicit mutation of the ONDTF core.
8. **Evidence-based mapping.** Compatibility is established through mapped outcomes and evidence, not terminology alone.

## Implementation relationships

The controlled taxonomy in `model/profiles/external-adoption-taxonomy.yaml` defines five relationships.

| Relationship | Meaning |
|---|---|
| `substitutable` | Multiple mechanisms may satisfy the same required capability and outcomes. |
| `complementary` | The mechanism adds a capability intended to operate alongside another selection. |
| `required-companion` | The mechanism must operate with a declared companion capability or dependency. |
| `profile-exclusive` | The profile authority constrains the profile to this mechanism for a documented reason. |
| `incompatible` | The mechanism cannot satisfy the mapped capability within the declared profile constraints. |

`required-companion`, `profile-exclusive`, and `incompatible` relationships require explicit justification. A profile-exclusive selection is a property of that profile, not of ONDTF generally.

## Live adoption versus illustration

The canonical `model/profiles/external-adoption-register.yaml` records real governed adoption decisions. Informative demonstrations belong outside that register. This prevents an example from accidentally acquiring normative or architectural authority.

The [multi-ecosystem portability example](../../examples/external-pattern-mappings/) compares a DTG portfolio illustration, an EUDI-style wallet environment, and an OpenID-Federation-style enterprise environment using the same ONDTF abstractions. The comparison is evidence of portability, not evidence that the ecosystems are equivalent.

## Dependency change signals

ONDTF governs the semantics of a dependency-change signal, not the source that produces it. A signal may originate from a standards-watch process, repository monitor, release feed, regulatory publication, security advisory, dependency scanner, or accountable human review.

The profile remains responsible for determining whether the signal changes requirements, evidence, interoperability assumptions, migration obligations or retirement decisions.

## Adoption test

Before approving an external mechanism, ask:

1. What ONDTF capability is being satisfied?
2. Which required outcomes remain invariant if the mechanism is replaced?
3. Which ONDTF requirements does the mechanism support?
4. Is the mechanism substitutable, complementary, required with another capability, profile-exclusive, or incompatible?
5. If alternatives are prohibited, what competent authority and evidence justify exclusivity?
6. Does the selection weaken any mandatory ONDTF obligation?
7. What source/version changes trigger review?
8. What evidence demonstrates the mapping?

[Previous: Guided Construction Readiness](guided-construction-readiness.md) · [Back to Adoption](index.md)
