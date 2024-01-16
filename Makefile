DOCKER_COMPOSE = docker compose
COMPOSE_FILE = "docker-compose-dev.yaml"
DOCKER = docker

ifneq ($(filter prod, $(MAKECMDGOALS)),)
	COMPOSE_FILE = "docker-compose-prod.yaml"
endif

ifneq ($(filter restart logs attach exec,$(MAKECMDGOALS)),)
	SERVICE = $(word 2, $(MAKECMDGOALS))
	EXEC_COMMAND = $(word 3, $(MAKECMDGOALS))
endif

.PHONY: help

help: 
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  ps          - show all containers"
	@echo "  build       - build all containers"
	@echo "  up          - start all containers"
	@echo "  down        - stop all containers"
	@echo "  restart-all - restart all containers"
	@echo 
	@echo "  restart backend|frontend|nginx           - restart service"
	@echo "  logs    backend|frontend|nginx           - show logs of service"
	@echo "  attach  backend|frontend|nginx           - attach to service"
	@echo "  exec    backend|frontend|nginx <command> - execute command in service"

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
