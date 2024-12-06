from sqlmodel import Session, select

from app.domain.models import Mission
from app.domain.models.mission import MissionCreate


class MissionsRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create(self, mission_create: MissionCreate) -> Mission:
        mission = Mission(**mission_create.model_dump())

        self.db.begin()

        self.db.add(mission)
        self.db.commit()
        self.db.refresh(mission)

        return mission

    async def get(self, mission_id: int) -> Mission:
        return self.db.exec(select(Mission).where(Mission.id == mission_id)).one()
