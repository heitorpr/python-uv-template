from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.api.v1.schemas.missions import MissionSchema
from app.domain.models import Hero, Mission

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


@router.put(
    "/{mission_id}/heroes/{hero_id}",
    summary="Assign a hero to a mission",
    description="Assign a hero to a mission by ID",
    tags=["missions"],
    response_model=MissionSchema,
    status_code=200,
)
def assign_hero_to_mission(mission_id: int, hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    mission = session.get(Mission, mission_id)
    if not hero or not mission:
        raise HTTPException(status_code=404, detail="Hero or Mission not found")

    mission.heroes.append(hero)
    session.add(mission)
    session.commit()

    session.refresh(mission)
    return mission
