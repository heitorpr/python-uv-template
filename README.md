# setup uv

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

# setup venv

```shell
uv venv
source .venv/bin/activate
uv sync
```


# setup pre-commit

```shell
uv run pre-commit install -f
uv run pre-commit install --hook-type commit-msg
```

# run project

```shell
uv run fastapi dev --port 8000 src/main.py
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
sudo chown -R $USER:$USER src/alembic/versions
```

# update all dependencies

```shell
rm uv.lock
uv lock
uv sync
```

# list outdated libs

```shell
uv run pip list --outdated
```

# run ipython

```shell
uv run ipython -i src/ipython_setup.py
```
