def generate_mermaid_diagram():
    from eralchemy import render_er
    from sqlmodel import SQLModel

    target_metadata = SQLModel.metadata
    filename = "src/alembic/db_mer.md"
    render_er(target_metadata, filename)
