install:
	poetry install
.PHONY: install

test:  ## Run tests
	poetry run pytest .
.PHONY: test

lint:  ## Run linting
	poetry run black --check ./src
	poetry run isort -c ./src
	poetry run flake8 ./src
	poetry run pydocstyle ./src
.PHONY: lint

lint-fix:  ## Run autoformatters
	poetry run black .
	poetry run isort .
.PHONY: lint-fix

typecheck:  ## Run typechecking
	poetry run mypy --show-error-codes --pretty .
.PHONY: typecheck