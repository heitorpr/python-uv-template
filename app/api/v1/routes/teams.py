from fastapi import APIRouter, HTTPException

from app.core.deps import SessionDep
from app.domain.models import Team

router = APIRouter()


@router.post(
    "/",
    summary="Create a team",
    description="Create a team with a name",
    tags=["teams"],
    response_model=Team,
    status_code=201,
)
async def create_team(team: Team, session: SessionDep):
    session.add(team)
    session.commit()
    session.refresh(team)
    return team


@router.get(
    "/{team_id}",
    summary="Read team",
    description="Read a team by ID",
    tags=["teams"],
    response_model=Team,
    status_code=200,
)
async def read_team(team_id: int, session: SessionDep):
    team = session.get(Team, team_id)

    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    return team
