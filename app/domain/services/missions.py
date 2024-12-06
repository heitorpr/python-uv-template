from app.api.v1.schemas import MissionPublic
from app.domain.models import Mission
from app.domain.models.mission import MissionCreate
from app.domain.repositories import HeroesRepository, MissionsRepository


class MissionsService:
    def __init__(self, mission_repository: MissionsRepository, hero_repository: HeroesRepository):
        self.mission_repository = mission_repository
        self.hero_repository = hero_repository

    async def _parse_to_public(self, mission: Mission) -> MissionPublic:
        heroes = await self.hero_repository.get_from_mission(mission.id)

        return MissionPublic(**{**mission.model_dump(), "heroes": heroes})

    async def create(self, mission_create: MissionCreate) -> MissionPublic:
        mission = await self.mission_repository.create(mission_create)
        return await self._parse_to_public(mission)

    async def get(self, mission_id: int) -> MissionPublic:
        mission = await self.mission_repository.get(mission_id)
        return await self._parse_to_public(mission)

    async def assign_hero(self, mission_id: int, hero_id: int) -> MissionPublic:
        mission = await self.mission_repository.get(mission_id)
        hero = await self.hero_repository.get(hero_id)

        await self.hero_repository.assign_to_mission(hero.id, mission.id)
        return await self._parse_to_public(mission)
