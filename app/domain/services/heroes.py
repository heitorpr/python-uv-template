from app.api.v1.schemas.heroes import HeroSchema
from app.domain.models.hero import HeroCreate
from app.domain.repositories import HeroesRepository


class HeroesService:
    def __init__(self, repository: HeroesRepository):
        self.repository = repository

    async def create_hero(self, hero_create: HeroCreate) -> HeroSchema:
        hero = await self.repository.create(hero_create)
        return HeroSchema(**hero.model_dump())

    async def read_hero(self, hero_id: int):
        hero = await self.repository.get(hero_id)
        return HeroSchema(**hero.model_dump())