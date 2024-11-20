from collections.abc import Generator

from sqlalchemy import create_engine
from sqlmodel import Session

from app.core.settings import settings

engine = create_engine(str(settings.db_dsn_sync), echo=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
