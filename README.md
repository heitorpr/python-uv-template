# setup uv

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```


# setup pre-commit

```shell
uv run pre-commit install -f
uv run pre-commit install --hook-type commit-msg
```

# setup venv

```shell
uv venv
source .venv/bin/activate
uv sync
```

# run project

```shell
uv run fastapi dev --port 8003 app/main.py
```

# run linters

```shell
uv run ruff check .
uv run pyright .
```

# run migrations
```shell
docker compose exec -it backend uv run alembic upgrade head
```

# create migrations

```shell
docker compose exec -it backend uv run alembic revision --autogenerate -m "init schema"
```
