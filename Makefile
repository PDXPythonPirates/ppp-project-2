# to boot the app run `flask run` after `make install`
install:
	@pip install --upgrade pip
	@pip install poetry==1.1.12
	@poetry install ${POETRY_ARGS}
	@poetry update
	@poetry shell
	@# configure the local git hooks path to run the path in the repo
	@# Alternative approach not used here since it depends on the git version 'git config core.hooksPath .githooks/hooks'
	@# By default this should point to the default path .git/hooks
	@chmod +x .githooks/hooks/pre-commit
	@find .git/hooks -type l -exec rm {} \;
	@find .githooks/hooks -type f -exec ln -sf ../../{} .git/hooks/ \;
	@chmod +x .git/hooks/pre-commit

test:
	python -m poetry run python -m pytest -v tests

up:
	@docker-compose up -d
	@echo "waiting for mysql container to fully boot ~ 30 sec"
	@sleep 30
	@open http://localhost:5000
	@docker logs --follow ppp-project-2

down:
	@docker-compose down
	@$(MAKE) stop

db:
	docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=pyrates -e MYSQL_USER=pyrates \
    -e MYSQL_PASSWORD=iamyourcaptain \
    mysql/mysql-server:5.7

# project docker container
project_name = ppp-project-2

# show the docker logs
logs:
	docker logs --follow $(project_name)
# stop all docker containers
stop:
	@if [[ $$(docker ps -aq) ]]; then\
		echo "Stopping Containers";\
        docker stop $$(docker ps -aq);\
    fi
	docker system prune -a --force
	docker volume prune --force

# print info about all commands in this makefile
define help_info

make install: 	installs poetry and boots virtual env
make test:      runs all tests
make up:		use docker compose to spin up the app and sql containers
make down:      use docker compose to shut down containers
make db:		build sql db container
make logs:    	tails the logs if you exited 
make stop:    	stops all running containers and prunes

endef
export help_info

help:
	@echo "$$help_info"
