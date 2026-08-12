# v0.7.0 validation notes

## Repository validation

The v0.7.0 tree was exercised locally against the repository validation stack after release consolidation.

Passed checks include:

- reference implementation: 5 assertions;
- v0.7 execution validation: 6 conformance assertions and evidence inventory consistency;
- Identifier Registry: 425 resolvable identifiers across 27 controlled classes, zero duplicate registry entries;
- schema-instance validation: 82 positive/negative checks across 15 schemas;
- release integrity and release-payload validation;
- terminology: 51 governed terms;
- repository publication coverage: 337 published Markdown pages;
- assurance/reference validation: 46 registered standards and instruments;
- data/privacy/rights validation;
- integration validation;
- maturation governance: 9 limitations, 20 issues, 7 programmes, 16 adoption patterns and 4 release gates;
- normative/governance: 28 requirements, 14 roles and 12 responsibility assignments;
- operations/conformance: 11 lifecycle states and 12 transitions;
- assurance/rights, profile/adoption, sector standards and worked-profile validation;
- Mermaid source validation: 127 diagrams parsed by repository source checks.

## Environment-limited checks

The local execution environment did not contain Bundler/Jekyll and could not reach RubyGems to install it, so a local Jekyll site build could not be completed. The Mermaid CLI full SVG-render pass was also unable to complete within the execution window, although all 127 Mermaid sources passed the repository parser and extraction step.

Both hosted workflows provision Node and Ruby explicitly and run the full Mermaid render, Jekyll build and built-site inspection. They have been updated so the new v0.7 execution and Identifier Registry validation gates execute before publication. This note records the distinction between locally observed evidence and checks that remain CI-executed; it does not represent unexecuted checks as passing.
