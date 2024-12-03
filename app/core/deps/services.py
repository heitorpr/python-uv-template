from fastapi import Depends

from app.core.deps.repositories import get_hero_repository
from app.domain.repositories import HeroesRepository
from app.domain.services import HeroesService


def get_heroes_service(
    repository: HeroesRepository = Depends(get_hero_repository)
) -> HeroesService:
    return HeroesService(repository)
