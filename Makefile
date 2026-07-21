.PHONY: validate site candidate-check
validate:
	python3 scripts/validate_repo.py
	python3 scripts/extract_mermaid.py
	bash scripts/validate_mermaid.sh
site:
	bundle exec jekyll build --trace
	python3 scripts/check_built_site.py
candidate-check: validate site
