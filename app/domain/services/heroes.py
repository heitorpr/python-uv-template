from app.api.v1.schemas import HeroPublic
from app.domain.models import Hero
from app.domain.models.hero import HeroCreate, HeroUpdate
from app.domain.repositories import HeroesRepository, TeamsRepository


class HeroesService:
    def __init__(self, hero_repository: HeroesRepository, team_repository: TeamsRepository):
        self.hero_repository = hero_repository
        self.team_repository = team_repository

    async def _parse_to_public(self, hero: Hero) -> HeroPublic:
        team = None
        if hero.team_id:
            team = await self.team_repository.get(hero.team_id)

        return HeroPublic(**{**hero.model_dump(), "team": team.model_dump() if team else None})

    async def create(self, hero_create: HeroCreate) -> HeroPublic:
        if hero_create.team_id and hero_create.team:
            raise ValueError("You can't pass both team_id and team")

        if hero_create.team:
            team = await self.team_repository.create(hero_create.team)
            hero_create.team_id = team.id

        hero = await self.hero_repository.create(hero_create)
        return await self._parse_to_public(hero)

    async def get(self, hero_id: int) -> HeroPublic:
        hero = await self.hero_repository.get(hero_id)
        return await self._parse_to_public(hero)

    async def update(self, hero_id: int, hero_data: HeroUpdate) -> HeroPublic:
        hero = await self.hero_repository.update(hero_id, hero_data)
        return await self._parse_to_public(hero)

    async def delete(self, hero_id: int) -> HeroPublic:
        hero = await self.hero_repository.delete(hero_id)
        return await self._parse_to_public(hero)

    async def assign_team(self, hero_id: int, team_id: int) -> HeroPublic:
        hero = await self.hero_repository.get(hero_id)
        team = await self.team_repository.get(team_id)

        hero.team_id = team.id
        await self.hero_repository.update(hero_id, HeroUpdate(**hero.model_dump()))
        return await self._parse_to_public(hero)
