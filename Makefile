### Base Development Environment ###
base_up:
	docker-compose -f compose/dev/db.yml up -d

base_down:
	docker-compose -f compose/dev/db.yml down --remove-orphans

### Run dev environmet ###
dev_up:
	docker-compose -f compose/dev/db.yml -f compose/dev/app.yml up -d

dev_down:
	docker-compose -f compose/dev/db.yml -f compose/dev/app.yml down --remove-orphans

rebuild_dev:
	docker-compose -f compose/dev/db.yml -f compose/dev/app.yml up --build app_dev

### Run Test in docker files ###
docker_test:
	docker-compose -f compose/test/testing.yml up --build --force-recreate \
		--exit-code-from app_testing

# Test without docker containers
test:
	pytest -v --cov=core/ --cov-report term-missing ./tests/
