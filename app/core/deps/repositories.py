from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps.db import get_session
from app.domain.repositories import HeroesRepository, MissionsRepository, TeamsRepository


def get_hero_repository(db: AsyncSession = Depends(get_session)) -> HeroesRepository:
    return HeroesRepository(db)


def get_team_repository(db: AsyncSession = Depends(get_session)) -> TeamsRepository:
    return TeamsRepository(db)


def get_mission_repository(db: AsyncSession = Depends(get_session)) -> MissionsRepository:
    return MissionsRepository(db)
