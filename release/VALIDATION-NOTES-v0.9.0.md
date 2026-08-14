# v0.9.0 Validation Notes

The release package passed repository-local candidate, schema, release-integrity, terminology, documentation, assurance/reference, data/privacy/rights, integration, maturation, normative/governance, operations/conformance, assurance/rights, profile/adoption, sector standards, worked-profile, release and Mermaid-source validation.

Two publication checks are environment-dependent in this execution environment:

- Mermaid CLI rendering could not complete because the local CLI dependency was not available and installation exceeded the execution window. GitHub Actions provisions Node and runs the render gate.
- Jekyll could not run locally because `bundle` is not installed in this sandbox. GitHub Actions provisions Ruby/Bundler and runs the Jekyll build plus built-site link inspection before Pages publication.

These limitations are tooling-environment limitations, not recorded as successful local checks.
