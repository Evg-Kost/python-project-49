install:
	uv sync
brain-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/brain*.whl
package-reinstall:
	uv tool install --force dist/brain*.whl
lint:
	uv run ruff check
check: lint


