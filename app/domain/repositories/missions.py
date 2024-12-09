from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.domain.models import Mission
from app.domain.models.mission import MissionCreate


class MissionsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, mission_create: MissionCreate) -> Mission:
        mission = Mission(**mission_create.model_dump())

        self.db.begin()

        self.db.add(mission)
        await self.db.commit()
        await self.db.refresh(mission)

        return mission

    async def get(self, mission_id: int) -> Mission:
        result = await self.db.execute(select(Mission).where(Mission.id == mission_id))
        return result.scalar_one()
