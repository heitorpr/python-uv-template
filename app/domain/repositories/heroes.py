from sqlmodel import Session

from app.domain.models.hero_association import Hero, HeroCreate


class HeroesRepository:
    def __init__(
        self,
        db: Session
    ):
        self.db = db

    async def create(self, hero_create: HeroCreate) -> Hero:
        hero = Hero(**hero_create.model_dump())

        self.db.add(hero)
        self.db.commit()
        self.db.refresh(hero)

        return hero
