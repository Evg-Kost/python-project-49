install:
	uv sync
brain-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/hexlet*.whl
package-reinstall:
	uv tool install --force dist/hexlet*.whl
lint:
	uv run ruff check
check: lint


