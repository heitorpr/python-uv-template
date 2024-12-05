from fastapi import Depends
from sqlmodel import Session

from app.core.deps.db import get_session
from app.domain.repositories import HeroesRepository
from app.domain.repositories.teams import TeamsRepository


def get_hero_repository(db: Session = Depends(get_session)) -> HeroesRepository:
    return HeroesRepository(db)


def get_team_repository(db: Session = Depends(get_session)) -> TeamsRepository:
    return TeamsRepository(db)
