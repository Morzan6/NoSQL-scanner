DOCKER_COMPOSE = docker compose
COMPOSE_FILE = "docker-compose-dev.yaml"
DOCKER = docker

ifneq ($(filter restart logs attach exec,$(MAKECMDGOALS)),)
	SERVICE = $(word 2, $(MAKECMDGOALS))
	EXEC_COMMAND = $(word 3, $(MAKECMDGOALS))
endif

ps:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) ps -a

build:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) build

up: 
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) up -d

down:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) down

restart-all:
	@$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) restart

restart:
	@$(DOCKER) restart $(SERVICE)

logs:
	@$(DOCKER) logs -f $(SERVICE) 

attach:
	@$(DOCKER) exec -it $(SERVICE) bash

exec:
	@$(DOCKER) exec $(SERVICE) $(EXEC_COMMAND)
