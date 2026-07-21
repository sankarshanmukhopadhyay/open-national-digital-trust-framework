---
title: Standards Profile
parent: Open National Digital Trust Framework
nav_order: 4
has_children: true
---

# Open Standards Profile

The ONDTF profiles standards; it does not create unnecessary substitutes.

## Standards families

| Concern | Preferred standards families |
|---|---|
| Credential data | W3C VC Data Model 2.0, SD-JWT VC, ISO mdoc |
| Identifiers and keys | W3C DID Core, Controlled Identifiers, HTTPS, X.509 |
| Issuance and presentation | OpenID4VCI, OpenID4VP, ISO 18013-7 |
| Authentication | WebAuthn, FIDO2, OpenID Connect, NIST 800-63 profiles |
| Secure messaging | TLS, OAuth 2.x profiles, DIDComm where justified |
| Status | Bitstring Status List, OCSP/CRL where applicable |
| Trust resolution | trust lists, PKI, OpenID Federation, TRQP-compatible registries |
| Policy | machine-readable policy profiles with deterministic versioning |
| Audit and evidence | signed event records, secure timestamps, transparency logs |
| Privacy | selective disclosure, pairwise identifiers, unlinkability controls |

## Multi-format requirement

A national ecosystem SHOULD support at least:

- W3C VC-compatible credentials for general-purpose attestations;
- SD-JWT VC for selective-disclosure token ecosystems;
- ISO mdoc for mobile identity documents and proximity use cases.

Interoperability MUST be achieved through explicit national profiles, protocol support and conformance testing, not by claiming that all formats are equivalent.
