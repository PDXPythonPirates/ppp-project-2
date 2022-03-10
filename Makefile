install:
	pip install --upgrade pip
	pip install poetry==1.1.12
	poetry install ${POETRY_ARGS}
	poetry shell
	# configure the local git hooks path to run the path in the repo
	git config core.hooksPath .githooks
