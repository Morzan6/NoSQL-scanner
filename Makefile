DOCKER_COMPOSE = docker compose

ifneq ($(filter build up down restart logs clean,$(MAKECMDGOALS)),)
	COMPOSE_FILE := "docker-compose-$(wordlist 2,2,$(MAKECMDGOALS)).yaml"
endif

build:
	@$(DOCKER_COMPOSE) -f "docker-compose-$<.yaml" build

up:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) up -d

down:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) down

restart:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) restart

logs:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) logs -f

exec:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) exec <SERVICE_NAME> <COMMAND>

clean:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) down -v
