from fastapi import APIRouter

from app.api.v1.schemas import TeamPublic
from app.core.deps import TeamsServiceDep
from app.domain.models.hero import HeroBase
from app.domain.models.team import TeamCreate, TeamUpdate

router = APIRouter()


@router.post(
    "/",
    summary="Create a team",
    description="Create a team with a name",
    tags=["teams"],
    response_model=TeamPublic,
    status_code=201,
)
async def create_team(team: TeamCreate, service: TeamsServiceDep):
    return await service.create(team)


@router.get(
    "/{team_id}",
    summary="Read team",
    description="Read a team by ID",
    tags=["teams"],
    response_model=TeamPublic,
    status_code=200,
)
async def read_team(team_id: int, service: TeamsServiceDep):
    return await service.get(team_id)


@router.put(
    "/{team_id}",
    summary="Update team",
    description="Update a team by ID",
    tags=["teams"],
    response_model=TeamPublic,
    status_code=200,
)
async def update_team(team_id: int, team_data: TeamUpdate, service: TeamsServiceDep):
    return await service.update(team_id, team_data)


@router.get(
    "/{team_id}/heroes",
    summary="List heroes",
    description="List all heroes in a team",
    tags=["teams"],
    response_model=list[HeroBase],
    status_code=200,
)
async def list_heroes(team_id: int, service: TeamsServiceDep):
    return await service.list_heroes(team_id)
