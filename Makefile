### Base Development Environment ###
dev_up:
	docker-compose -f compose/dev/db.yml up -d

dev_down:
	docker-compose -f compose/dev/db.yml down --remove-orphans
