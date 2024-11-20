from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.api.deps import SessionDep
from app.domain.models import Hero, Mission, Team
from app.domain.schemas.hero_association import HeroSchema, MissionSchema

router = APIRouter()


@router.post(
    "/heroes/",
    summary="Create a hero",
    description="Create a hero with all the information",
    tags=["heroes"],
    response_model=HeroSchema,
    status_code=201,
)
async def create_hero(hero: Hero, session: SessionDep):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


@router.get(
    "/heroes/",
    summary="Read heroes",
    description="Read all heroes",
    tags=["heroes"],
    response_model=list[HeroSchema],
    status_code=200,
)
async def read_heroes(session: SessionDep):
    return session.exec(select(Hero)).all()


@router.get(
    "/heroes/{hero_id}",
    summary="Read a hero",
    description="Read a hero by ID",
    tags=["heroes"],
    response_model=HeroSchema,
    status_code=200,
)
async def read_hero(hero_id: int, session: SessionDep):
    statement = select(Hero).where(Hero.id == hero_id)
    return session.exec(statement).one()


@router.put(
    "/heroes/{hero_id}",
    summary="Update a hero",
    description="Update a hero by ID",
    tags=["heroes"],
    response_model=Hero,
    status_code=200,
)
async def update_hero(hero_id: int, hero_data: Hero, session: SessionDep):
    db_hero = session.get(Hero, hero_id)

    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    for key, value in hero_data.model_dump(exclude_unset=True).items():
        setattr(db_hero, key, value)

    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@router.delete(
    "/heroes/{hero_id}",
    summary="Delete a hero",
    description="Delete a hero by ID",
    tags=["heroes"],
    status_code=204,
)
async def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)

    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    session.delete(hero)
    session.commit()
    return


@router.post(
    "/teams/",
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
    "/teams/{team_id}",
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


@router.post(
    "/missions/",
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
    "/missions/{mission_id}/heroes/{hero_id}",
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
