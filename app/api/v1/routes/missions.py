from fastapi import APIRouter

from app.api.v1.schemas import MissionPublic
from app.core.deps import MissionsServiceDep
from app.domain.models.mission import MissionCreate

router = APIRouter()


@router.post(
    "/",
    summary="Create a mission",
    description="Create a mission with a name and description",
    tags=["missions"],
    response_model=MissionPublic,
    status_code=201,
)
async def create_mission(mission: MissionCreate, service: MissionsServiceDep):
    return await service.create(mission)


@router.get(
    "/{mission_id}",
    summary="Read mission",
    description="Read a mission by ID",
    tags=["missions"],
    response_model=MissionPublic,
    status_code=200,
)
async def read_mission(mission_id: int, service: MissionsServiceDep):
    return await service.get(mission_id)


@router.put(
    "/{mission_id}/assign-hero/{hero_id}",
    summary="Assign a hero to a mission",
    description="Assign a hero to a mission by ID",
    tags=["missions"],
    response_model=MissionPublic,
    status_code=200,
)
async def assign_hero(mission_id: int, hero_id: int, service: MissionsServiceDep):
    return await service.assign_hero(mission_id, hero_id)
