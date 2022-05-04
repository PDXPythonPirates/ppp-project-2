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

build:
	@# suppress the docker scan message then build
	@export DOCKER_SCAN_SUGGEST=false; \
	docker build -t ppp-project-2 .

db:
	docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=pyrates -e MYSQL_USER=pyrates \
    -e MYSQL_PASSWORD=iamyourcaptain \
    mysql/mysql-server:5.7

run:
	@# TODO: need to merge PR that checks for the specific container
	@# TODO: think about checking container health: https://scoutapm.com/blog/how-to-use-docker-healthcheck
	@if [[ $$(docker ps -aq) ]]; then \
		echo "Containers Already Running";\
		docker ps;\
    else \
        echo "Booting Container"; \
		docker run -d -p 5000:5000 --name ppp-project-2 ppp-project-2 --link mysql:dbserver \
		-e DATABASE_URL=mysql+pymysql://pyrates:iamyourcaptain@dbserver/pyrates pyrates:latest;\
		sleep 5;\
		open http://localhost:5000;\
		docker logs --follow ppp-project-2;\
    fi

logs:
	docker logs --follow ppp-project-2

stop:
	@if [[ $$(docker ps -aq) ]]; then\
		echo "Stopping Containers";\
        docker stop $$(docker ps -aq);\
    fi
	docker system prune -a --force
	docker volume prune --force

define help_info

make install: 	installs poetry and boots virtual env
make test:      runs all tests
make build:   	builds docker containers
make run:		build sql db container
make run:     	boots the containers on local port 5000 and opens page
make logs:    	tails the logs if you exited 
make stop:    	stops all running containers and prunes

endef
export help_info

help:
	@echo "$$help_info"
