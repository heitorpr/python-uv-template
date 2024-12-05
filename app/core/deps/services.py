from fastapi import Depends

from app.core.deps.repositories import get_hero_repository, get_team_repository
from app.domain.repositories import HeroesRepository
from app.domain.repositories.teams import TeamsRepository
from app.domain.services import HeroesService, TeamsService


def get_heroes_service(
    hero_repository: HeroesRepository = Depends(get_hero_repository),
    team_repository: TeamsRepository = Depends(get_team_repository),
) -> HeroesService:
    return HeroesService(hero_repository=hero_repository, team_repository=team_repository)


def get_teams_service(
    hero_repository: HeroesRepository = Depends(get_hero_repository),
    teams_repository: TeamsRepository = Depends(get_team_repository),
) -> TeamsService:
    return TeamsService(hero_repository=hero_repository, teams_repository=teams_repository)
