# Open National Digital Trust Framework (ONDTF)

[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://sankarshanmukhopadhyay.github.io/open-national-digital-trust-framework/)
[![Status](https://img.shields.io/badge/status-initial%20public%20draft-orange)](RELEASE_NOTES.md)
[![Version](https://img.shields.io/badge/version-v0.2.0-green)](CHANGELOG.md)

The **Open National Digital Trust Framework (ONDTF)** is a jurisdiction-neutral, multi-sector reference framework for governing, implementing, assuring, and interoperating digital trust infrastructure.

ONDTF treats trust as an operational system property. It connects identity, authority, policy, evidence, assurance, decision, effect, accountability, and redress without requiring a single identity system, credential format, registry, protocol, or technology provider.

## What problem does this solve?

National digital programmes often provide identity, authentication, payments, data exchange, credentials, or registries independently. They rarely provide one coherent model for determining:

- who or what is acting;
- under whose authority;
- within which policy and jurisdiction;
- using what evidence;
- with what assurance;
- producing which attributable effect;
- and through which challenge, revocation, and remedy path.

ONDTF supplies that missing governance and architecture layer.

## Repository status

| Attribute | Value |
|---|---|
| Portfolio role | Jurisdiction-neutral national framework |
| Lifecycle | Active initial public draft |
| Current version | v0.2.0 |
| Stability | Experimental; architecture under review |
| Primary artefact | Framework, reference architecture, and profile method |
| Normative posture | Normative requirements are explicitly labelled |
| India material | Illustrative jurisdiction profile under `profiles/india/` |
| Validation | `python3 scripts/validate_repo.py` |

## Framework independence and optional compatibility

ONDTF is self-contained at the framework level, implementation-neutral at the architecture level, and extensible through jurisdiction, sector, and technical profiles. Core adoption does not require any particular external meta-model, schema suite, protocol, registry product, or software stack.

Two related projects provide optional implementation accelerators:

- **[Trust Systems Meta-Model (TSMM)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model):** a compatible reference meta-model that may be used for deeper semantic formalisation.
- **[Trust Infrastructure Schemas (TIS)](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas):** a compatible schema suite that may be selected by an implementation or profile for portable machine-readable artefacts.

```mermaid
flowchart TB
    CORE[ONDTF core requirements]
    PROFILE[Jurisdiction or sector profile]
    IMPL[Conforming implementation]
    TSMM[Optional TSMM alignment]
    TIS[Optional TIS schema profile]
    ALT[Alternative compatible models and schemas]
    CORE --> PROFILE
    PROFILE --> IMPL
    TSMM -.-> IMPL
    TIS -.-> IMPL
    ALT -.-> IMPL
```

See [Framework independence](docs/foundations/framework-independence.md), [Portfolio alignment](docs/foundations/portfolio-alignment.md), and [Dependency policy](docs/foundations/dependency-policy.md).

## Start here

- [Policy and regulatory readers](docs/adoption/policy-reader-path.md)
- [Architects](docs/adoption/architect-reader-path.md)
- [Implementers](docs/adoption/implementer-reader-path.md)
- [Assurance and audit teams](docs/adoption/assurance-reader-path.md)
- [India profile](profiles/india/index.md)

## Ten-minute validation

```bash
gem install bundler
bundle install
python3 scripts/validate_repo.py
python3 scripts/extract_mermaid.py
bash scripts/validate_mermaid.sh
bundle exec jekyll build
python3 scripts/check_built_site.py
```

## Scope boundary

ONDTF does **not** define a national identity system, mandate a credential format, create legal recognition by itself, replace sector regulators, or centralise all trust decisions in one registry. It defines the common framework within which such systems can interoperate and be governed.

## Licensing

Documentation is licensed under [CC BY-NC-SA 4.0](LICENSE). Code and executable examples may be separately licensed in later releases.
