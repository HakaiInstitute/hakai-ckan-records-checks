run-hakai:
	poetry run python hakai_ckan_records_checks -c https://catalogue.hakai.org

run-hakai-no-cache:
	poetry run python hakai_ckan_records_checks -c https://catalogue.hakai.org --no-cache