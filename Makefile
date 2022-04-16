test:
	docker-compose run --rm --entrypoint pytest hacklights-web
compile:
	docker-compose run --rm --entrypoint pip-compile hacklights-web
format:
	docker-compose run --rm --entrypoint "black . && flake8" hacklights-web