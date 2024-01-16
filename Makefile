DOCKER_COMPOSE = docker compose
DOCKER = docker

ifneq ($(filter ps build up down restart-all ,$(MAKECMDGOALS)),)
	COMPOSE_FILE = "docker-compose-$(word 2, $(MAKECMDGOALS)).yaml"
endif

ifneq ($(filter logs attach exec,$(MAKECMDGOALS)),)
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

logs:
	$(DOCKER) logs -f $(SERVICE) 

attach:
	@$(DOCKER) exec -it $(SERVICE) bash

exec:
	@$(DOCKER) exec $(SERVICE) $(EXEC_COMMAND)
