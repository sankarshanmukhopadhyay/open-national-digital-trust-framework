---
title: Standards Profile
parent: Open National Digital Trust Framework
nav_order: 5
has_children: true
---

# Open standards profile

ONDTF profiles established standards and specifications; it does not create unnecessary substitutes. The [central standards, specifications and guidelines register](references.md) is the canonical place for publication status, edition, classification and source links.

## Standards families

| Concern | Referenced families |
|---|---|
| Credential data | [W3C VC Data Model 2.0](references.md#ref-W3C-VC-DM-2.0), SD-JWT-based profiles, [ISO mdoc](references.md#ref-ISO-IEC-18013-5-2021) |
| Identifiers and keys | [W3C DID Core](references.md#ref-W3C-DID-CORE-1.0), [Controlled Identifiers](references.md#ref-W3C-CONTROLLED-IDENTIFIERS-1.0), HTTPS and [X.509 PKI](references.md#ref-IETF-RFC-5280) |
| Issuance and presentation | [OpenID4VCI](references.md#ref-OIDF-OID4VCI-1.0), [OpenID4VP](references.md#ref-OIDF-OID4VP-1.0), [ISO 18013-7](references.md#ref-ISO-IEC-18013-7-2025) |
| Authentication | [WebAuthn](references.md#ref-W3C-WEBAUTHN-3), [FIDO2](references.md#ref-FIDO2), [OpenID Connect](references.md#ref-OIDF-OIDC-CORE-1.0), [NIST SP 800-63-4](references.md#ref-NIST-SP-800-63-4) profiles |
| Secure messaging | [TLS 1.3](references.md#ref-IETF-RFC-8446), [OAuth 2.0](references.md#ref-IETF-RFC-6749) security profiles and other profile-selected mechanisms |
| Status | [Bitstring Status List](references.md#ref-W3C-BITSTRING-STATUS-LIST-1.0), X.509 CRLs and equivalent profile-selected mechanisms |
| Trust resolution | [ETSI Trusted Lists](references.md#ref-ETSI-TS-119-612), PKI, [OpenID Federation](references.md#ref-OIDF-OPENID-FEDERATION-1.0) and governed registries |
| Policy | Machine-readable policy profiles with deterministic versioning and, where selected, [AuthZEN](references.md#ref-OIDF-AUTHZEN-API-1.0) interfaces |
| Audit and evidence | Signed event records, secure timestamps, provenance and transparency mechanisms selected by profile |
| Privacy | Selective disclosure, pairwise identifiers, unlinkability and privacy-risk controls |

## Multi-format requirement

A national ecosystem SHOULD support the credential formats required by its use cases and interoperability obligations. W3C VC, SD-JWT-based credentials and ISO mdoc are not presumed equivalent. Profiles MUST define transformations, proof semantics, status handling, holder binding, privacy properties and conformance expectations explicitly.

## Reference governance

- [Standards, Specifications and Guidelines Register](references.md)
- [Standards Alignment Method](alignment-method.md)
- [Sectoral Standards Adoption Strategy](sectoral-adoption-strategy.md)
- [NIST CSF 2.0 Mapping](nist-csf-mapping.md)
- [Security and Risk Control Alignment](iso-nist-control-alignment.md)
