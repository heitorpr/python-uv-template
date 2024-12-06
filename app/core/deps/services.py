from fastapi import Depends

from app.core.deps.repositories import (
    get_hero_repository,
    get_mission_repository,
    get_team_repository,
)
from app.domain.repositories import HeroesRepository, MissionsRepository, TeamsRepository
from app.domain.services import HeroesService, TeamsService
from app.domain.services.missions import MissionsService


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


def get_missions_service(
    hero_repository: HeroesRepository = Depends(get_hero_repository),
    mission_repository: MissionsRepository = Depends(get_mission_repository),
) -> MissionsService:
    return MissionsService(hero_repository=hero_repository, mission_repository=mission_repository)
