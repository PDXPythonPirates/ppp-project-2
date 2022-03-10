install:
	pip install --upgrade pip
	pip install poetry==1.1.12
	poetry install ${POETRY_ARGS}
	poetry shell
	# configure the local git hooks path to run the path in the repo
	chmod +x .githooks/hooks/*
	find .git/hooks -type l -exec rm {} \;
  	find .githooks -type f -exec ln -sf ../../{} .git/hooks/ \;
