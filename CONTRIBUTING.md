# Contributing

Contributions are welcome from government, standards, industry, civil-society, research and implementation communities.

## Contribution types

- Architecture and governance improvements
- Standards profiling and interoperability mappings
- Sector-specific requirements
- Threat models and assurance controls
- Reference implementation guidance
- Test cases, conformance criteria and diagrams
- Editorial corrections

## Principles

Contributions should remain vendor-neutral, implementation-neutral and aligned with open standards. They should distinguish normative requirements from informative guidance and avoid embedding a single institutional or technical model as the only valid path.

## Process

1. Open an issue describing the problem, proposition, scope, and acceptance criteria.
2. For substantial changes, identify the affected framework layers, stakeholders, authority boundaries, compatibility impact, and evidence that could falsify the proposed approach.
3. Submit a pull request with the smallest coherent implementation, rationale, evidence, and residual risk.
4. Add or update tests/validation for consequential claims and important negative or boundary cases.
5. Update diagrams, navigation, conformance requirements, examples, and release notes where relevant.
6. Confirm the repository validation and GitHub Pages build complete successfully before merge.
7. Merge only after the issue acceptance criteria are satisfied and the judgment that should remain visible is preserved in the issue, PR, tests, or durable documentation.

Substantive changes therefore follow **Issue → PR → tests/evidence → merge/release**. Trivial editorial changes may use a lighter path when they do not alter normative meaning, compatibility, authority, assurance, or release behaviour.

## Change titles

Prefer typed titles of the form:

```text
<type>(<scope>): <imperative summary>
```

Use `!` before `:` for consumer-visible breaking changes. Typical types are `feat`, `fix`, `docs`, `test`, `chore`, `refactor`, `ci`, `security`, and `governance`.

## Validation

Run the repository's documented validation path before submitting substantive work. The shortest current validation path is listed in `README.md`; CI remains the authoritative merge evidence for the submitted revision.

## Security and support

Do not disclose exploitable vulnerabilities in public issues; follow [SECURITY.md](SECURITY.md). General support and routing guidance is in [SUPPORT.md](SUPPORT.md).

## Style

Use clear, formal prose. Use **MUST**, **SHOULD** and **MAY** only where normative meaning is intended. Define acronyms on first use. Prefer diagrams for multi-party flows and state transitions.
