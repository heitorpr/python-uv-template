from fastapi import APIRouter

from app.core.deps import SessionDep
from app.domain.models import Mission

router = APIRouter()


@router.post(
    "/",
    summary="Create a mission",
    description="Create a mission with a name and description",
    tags=["missions"],
    response_model=Mission,
    status_code=201,
)
async def create_mission(mission: Mission, session: SessionDep):
    session.add(mission)
    session.commit()
    session.refresh(mission)
    return mission
