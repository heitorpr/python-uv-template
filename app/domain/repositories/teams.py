from sqlmodel import Session, select

from app.domain.models import Team
from app.domain.models.team import TeamCreate, TeamUpdate


class TeamsRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create(self, team_create: TeamCreate) -> Team:
        team = Team(**team_create.model_dump())

        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)

        return team

    async def get(self, team_id: int) -> Team:
        return self.db.exec(select(Team).where(Team.id == team_id)).one()

    async def update(self, team_id: int, team_data: TeamUpdate) -> Team:
        team = await self.get(team_id)

        for key, value in team_data.model_dump(exclude_unset=True).items():
            setattr(team, key, value)

        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)

        return team
