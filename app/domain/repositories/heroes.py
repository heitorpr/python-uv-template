from sqlmodel import Session, select

from app.domain.models.hero import HeroCreate
from app.domain.models.hero_association import Hero, HeroMissionLink, Mission, Team


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
        hero, team = self.db.exec(select(Hero, Team).join(Team).where(Hero.id == hero_id)).one()

        hero.team = team

        missions = self.db.exec(
            select(Mission, HeroMissionLink)
            .join(HeroMissionLink)
            .where(HeroMissionLink.hero_id == hero_id)
            .where(Mission.id == HeroMissionLink.mission_id)
        ).all()

        hero.missions = [mission for mission, link in missions]
        return hero
