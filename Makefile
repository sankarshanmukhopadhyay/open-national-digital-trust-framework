.PHONY: terminology validate site candidate-check v070-check v090-check
terminology:
	python3 scripts/build_terminology.py
	python3 scripts/validate_terminology.py
validate:
	python3 scripts/validate_v070_execution.py
	python3 scripts/validate_rahp_closure.py
	python3 scripts/validate_interoperability_candidate.py
	python3 scripts/validate_candidate_specification.py
	python3 scripts/build_requirements_register.py
	python3 scripts/build_identifier_registry.py
	python3 scripts/validate_identifier_registry.py
	python3 scripts/validate_requirements_register.py
	python3 scripts/validate_schema_instances.py
	python3 scripts/validate_release_integrity.py
	python3 scripts/validate_terminology.py
	python3 scripts/validate_repo.py
	python3 scripts/validate_maturity.py
	python3 scripts/validate_v1_readiness.py
	python3 scripts/validate_assurance_references.py
	python3 scripts/validate_data_privacy_rights.py
	python3 scripts/validate_integration.py
	python3 scripts/validate_maturation.py
	python3 scripts/validate_normative_governance.py
	python3 scripts/validate_operations_conformance.py
	python3 scripts/validate_assurance_rights.py
	python3 scripts/validate_profile_adoption.py
	python3 scripts/validate_jurisdiction_exemplars.py
	python3 scripts/validate_sector_standards.py
	python3 scripts/validate_worked_profile.py
	python3 scripts/validate_release.py
	python3 scripts/check_mermaid_source.py
	python3 scripts/extract_mermaid.py
	bash scripts/validate_mermaid.sh
site:
	bundle exec jekyll build --trace
	python3 scripts/check_built_site.py
candidate-check: validate site
v070-check:
	python3 scripts/validate_v070_execution.py
v090-check:
	python3 scripts/validate_interoperability_candidate.py
	python3 scripts/validate_candidate_specification.py
	python3 scripts/validate_release.py
