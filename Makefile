install:
	uv sync
brain-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl
package-reinstall:
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl
test:
	uv run pytest
test-coverage:
	uv run pytest --cov=brain_games --cov-report xml
lint:
	uv run ruff check
check: test lint


