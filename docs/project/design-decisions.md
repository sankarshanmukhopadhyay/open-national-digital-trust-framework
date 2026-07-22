---
layout: default
title: Design Decisions
parent: Project Governance and Releases
nav_order: 4
---

# Design decisions

This page summarises architectural decisions that shape the framework and should not be reopened casually during editorial refinement.

| Decision | Consequence |
|---|---|
| Identity is distinct from authority | Strong authentication does not establish mandate or legitimate exercise. |
| Governance must remain visible at decision and effect time | Evidence, policy, responsibility and remedy cannot be confined to enrolment. |
| The core is technology neutral | Credential, identifier, registry and transport technologies are selected by profiles. |
| Standards are classified, not treated as universally normative | Foundational, profile-dependent, informative and jurisdictional references have different force. |
| Trust data is a protected asset class | Corruption of authority, status, policy or assurance data can create illegitimate effects. |
| Security and privacy are related but distinct | Secure processing may still be unnecessary, disproportionate or excessively linkable. |
| Affected parties extend beyond transaction participants | Challenge, explanation and remedy must account for externalised consequences. |
| Assurance is continuous | Material change, incidents, expired evidence and control degradation can invalidate prior confidence. |
| Conformance is evidence based | Self-description and technical interoperability alone are insufficient. |

Detailed rationale remains in the relevant architecture, governance, security, privacy and assurance pages.
