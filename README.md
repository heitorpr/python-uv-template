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
uv run fastapi dev --port 8000 app/main.py
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

# fix migrated created file permission

```shell
sudo chown -R $USER:$USER app/alembic/versions
```

# update all dependencies

```shell
rm uv.lock
uv lock
uv sync
```
