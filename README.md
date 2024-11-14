# setup pre-commit

```python
uv run pre-commit install -f
uv run pre-commit install --hook-type commit-msg
```

# run project

```python
uv run fastapi dev --port 8003 app/main.py
```

# run linters

```python
uv run ruff check .
uv run pyright .
```

# run migrations

```python
PYTHONPATH=. uv run alembic revision --autogenerate -m "init schema"
```
