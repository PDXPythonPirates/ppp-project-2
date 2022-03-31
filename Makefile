install:
	pip install --upgrade pip
	pip install poetry==1.1.12
	poetry install ${POETRY_ARGS}
	poetry shell
	# configure the local git hooks path to run the path in the repo
	# Alternative approach not used here since it depends on the git version 'git config core.hooksPath .githooks/hooks'
	# By default this should point to the default path .git/hooks
	chmod +x .githooks/hooks/pre-commit
	find .git/hooks -type l -exec rm {} \;
	find .githooks/hooks -type f -exec ln -sf ../../{} .git/hooks/ \;
	chmod +x .git/hooks/pre-commit

test:
	python -m poetry run python -m pytest -v tests

build:
	docker build -t ppp-project-2 .

run:
	@if [[ $$(docker ps -aq) ]]; then \
        echo "Containers Already Running";\
		docker ps;\
    else \
        echo "Booting Container"; \
		docker run -d -p 5000:5000 --name ppp-project-2 ppp-project-2;\
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
make run:     	boots the containers on local port 5000 and open page
make logs:    	tails the logs if you exited 
make stop:    	stops all running containers and prunes

endef
export help_info

help:
	@echo "$$help_info"
