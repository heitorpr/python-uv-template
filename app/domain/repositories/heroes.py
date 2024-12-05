from sqlmodel import Session, select

from app.domain.models import Hero
from app.domain.models.hero import HeroCreate, HeroUpdate


class HeroesRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create(self, hero_create: HeroCreate) -> Hero:
        hero = Hero(**hero_create.model_dump())

        self.db.add(hero)
        self.db.commit()
        self.db.refresh(hero)

        return hero

    async def get(self, hero_id: int) -> Hero:
        return self.db.exec(select(Hero).where(Hero.id == hero_id)).one()

    async def get_from_team(self, team_id: int) -> list[Hero]:
        return list(self.db.exec(select(Hero).where(Hero.team_id == team_id)).all())

    async def update(self, hero_id: int, hero_data: HeroUpdate) -> Hero:
        hero = await self.get(hero_id)

        for key, value in hero_data.model_dump(exclude_unset=True).items():
            setattr(hero, key, value)

        self.db.add(hero)
        self.db.commit()
        self.db.refresh(hero)
        return hero

    async def delete(self, hero_id: int):
        hero = await self.get(hero_id)
        self.db.delete(hero)
        self.db.commit()
        return hero
