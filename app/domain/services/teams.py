from app.api.v1.schemas import TeamPublic
from app.domain.models.hero import HeroBase
from app.domain.models.team import TeamCreate, TeamUpdate
from app.domain.repositories.heroes import HeroesRepository
from app.domain.repositories.teams import TeamsRepository


class TeamsService:
    def __init__(self, teams_repository: TeamsRepository, hero_repository: HeroesRepository):
        self.teams_repository = teams_repository
        self.hero_repository = hero_repository

    async def create(self, team_create: TeamCreate) -> TeamPublic:
        team = await self.teams_repository.create(team_create)
        return TeamPublic(**team.model_dump())

    async def get(self, team_id: int) -> TeamPublic:
        team = await self.teams_repository.get(team_id)
        return TeamPublic(**team.model_dump())

    async def update(self, team_id: int, team_data: TeamUpdate) -> TeamPublic:
        team = await self.teams_repository.update(team_id, team_data)
        return TeamPublic(**team.model_dump())

    async def list_heroes(self, team_id: int) -> list[HeroBase]:
        heroes = await self.hero_repository.get_from_team(team_id)
        return [HeroBase(**hero.model_dump()) for hero in heroes]
