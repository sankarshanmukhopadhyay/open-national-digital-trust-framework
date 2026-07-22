.PHONY: validate site candidate-check
validate:
	python3 scripts/validate_repo.py
	python3 scripts/validate_assurance_references.py
	python3 scripts/validate_data_privacy_rights.py
	python3 scripts/validate_integration.py
	python3 scripts/validate_maturation.py
	python3 scripts/validate_normative_governance.py
	python3 scripts/validate_operations_conformance.py
	python3 scripts/validate_assurance_rights.py
	python3 scripts/validate_release.py
	python3 scripts/check_mermaid_source.py
	python3 scripts/extract_mermaid.py
	bash scripts/validate_mermaid.sh
site:
	bundle exec jekyll build --trace
	python3 scripts/check_built_site.py
candidate-check: validate site
