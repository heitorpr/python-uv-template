from fastapi import Depends
from sqlmodel import Session

from app.core.deps.db import get_session
from app.domain.repositories import HeroesRepository


def get_hero_repository(db: Session = Depends(get_session)) -> HeroesRepository:
    return HeroesRepository(db)
