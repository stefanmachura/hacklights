test:
	docker-compose run --rm --entrypoint pytest hacklights-web
compile:
	docker-compose run --rm --entrypoint pip-compile hacklights-web
format:
	docker-compose run --rm --entrypoint "black . && isort --overwrite-in-place . && flake8" hacklights-web

db:
	docker exec -it  hacklights-hacklights-db-1 psql -U postgres
