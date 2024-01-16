DOCKER_COMPOSE = docker compose
COMPOSE_FILE = "docker-compose-dev.yaml"
DOCKER = docker

.PHONY: help

help: 
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  ps    - list all containers"
	@echo "  build - build all containers"
	@echo "  up    - start all containers"
	@echo "  down  - stop all containers"
	@echo 
	@echo "  restart-all              - restart all containers"
	@echo "  restart <service>        - restart service"
	@echo "  logs <service>           - show logs of service"
	@echo "  attach <service>         - attach to service"
	@echo "  exec <service> <command> - execute command in service"


ifneq ($(filter prod, $(MAKECMDGOALS)),)
	COMPOSE_FILE = "docker-compose-prod.yaml"
endif


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
