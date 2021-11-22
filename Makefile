### Base Development Environment ###
dev_up:
	docker-compose -f compose/dev/db.yml up -d

dev_down:
	docker-compose -f compose/dev/db.yml down --remove-orphans

docker_test:
	docker-compose -f compose/test/testing.yml up --build --force-recreate \
		--exit-code-from app_testing

test:
	pytest -v --cov=core/ --cov-report term-missing ./tests/
