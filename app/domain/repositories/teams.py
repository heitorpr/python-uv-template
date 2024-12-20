from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.domain.models import Team
from app.domain.models.team import TeamCreate, TeamUpdate


class TeamsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, team_create: TeamCreate) -> Team:
        team = Team(**team_create.model_dump())

        self.db.add(team)
        await self.db.commit()
        await self.db.refresh(team)

        return team

    async def create_list(self, team_create_list: list[TeamCreate]) -> list[Team]:
        teams = [Team(**team.model_dump()) for team in team_create_list]

        self.db.add_all(teams)
        await self.db.commit()

        return teams

    async def get(self, team_id: int) -> Team:
        result = await self.db.execute(select(Team).where(Team.id == team_id))
        return result.scalar_one()

    async def update(self, team_id: int, team_data: TeamUpdate) -> Team:
        team = await self.get(team_id)

        for key, value in team_data.model_dump(exclude_unset=True).items():
            setattr(team, key, value)

        self.db.add(team)
        await self.db.commit()
        await self.db.refresh(team)

        return team
