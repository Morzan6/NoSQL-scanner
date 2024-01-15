dev:
	docker compose -f docker-compose-dev.yaml up -d --build
down-dev:
	docker compose -f docker-compose-dev.yaml down

prod:
	docker compose up -d --build
down-prod:
	docker compose down
