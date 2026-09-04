# Security Policy

Do not disclose exploitable vulnerabilities in public issues.

Report security concerns privately to the repository maintainers using GitHub's private vulnerability reporting surface when available. A valid report should include the affected document or reference component, threat scenario, expected impact and recommended mitigation.

This repository contains specifications and examples rather than a production service. Security reports may therefore concern unsafe protocol profiles, ambiguous trust assumptions, privacy leakage, governance bypass, registry compromise or implementation guidance likely to create systemic risk.

## Supported versions

Security and safety fixes are applied to the current supported candidate line on `main` and to the latest published release when a release branch or patch is required. Older superseded candidate versions are not maintained unless a security notice explicitly says otherwise.

| Version | Supported |
|---|---|
| Current `main` candidate | Yes |
| Latest published release | Yes |
| Superseded releases | No, unless explicitly stated |

## Disclosure and handling

Maintainers will assess whether a report affects normative framework text, examples, schemas, validation tooling, or deployment guidance. Public disclosure should occur only after a safe remediation or an explicit decision that coordinated disclosure is unnecessary.
