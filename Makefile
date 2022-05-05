install:
	@pip install --upgrade pip
	@pip install poetry==1.1.12
	@poetry install ${POETRY_ARGS}
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
	docker-compose up -d; \
	sleep 5;\
	open http://localhost:5000;\
	docker logs --follow ppp-project-2;\

down:
	docker-compose down
	$(MAKE) stop

build:
	@# suppress the docker scan message then build
	@export DOCKER_SCAN_SUGGEST=false; \
	docker build -t ppp-project-2 .

db:
	docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=pyrates -e MYSQL_USER=pyrates \
    -e MYSQL_PASSWORD=iamyourcaptain \
    mysql/mysql-server:5.7

# build docker container
project_name = ppp-project-2
build:
	@# suppress the docker scan message then build
	@export DOCKER_SCAN_SUGGEST=false; \
	docker build -t $(project_name) .
  
# run the docker container if it is not already running
run:
	@# TODO: need to merge PR that checks for the specific container
	@# TODO: think about checking container health: https://scoutapm.com/blog/how-to-use-docker-healthcheck
	@if [[ $$(docker ps -aq -f "name"="$(project_name)") ]]; then \
		echo "   ";\
		echo "Project container already running";\
		echo "   ";\
		docker ps;\
		echo "   ";\
    else \
		echo "   ";\
        echo "Booting Container"; \
		docker run -d -p 5000:5000 --name $(project_name) $(project_name) --link mysql:dbserver \
		-e DATABASE_URL=mysql+pymysql://pyrates:iamyourcaptain@dbserver/pyrates pyrates:latest;\
		sleep 5;\
		open http://localhost:5000;\
		docker logs --follow $(project_name);\
	fi
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
make build:   	builds docker containers
make db:		build sql db container
make run:     	boots the containers on local port 5000 and opens page
make logs:    	tails the logs if you exited 
make stop:    	stops all running containers and prunes

endef
export help_info

help:
	@echo "$$help_info"
