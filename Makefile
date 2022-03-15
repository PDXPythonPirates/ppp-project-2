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
