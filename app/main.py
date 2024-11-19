from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import ORJSONResponse
from sqlmodel import Session, create_engine, select

from app.core.settings import settings
from app.domain.models import Hero, Mission, Team
from app.domain.schemas.hero_association import HeroSchema, MissionSchema

app = FastAPI(default_response_class=ORJSONResponse)
engine = create_engine(str(settings.db_dsn_sync), echo=True)


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post(
    "/heroes/",
    summary="Create a hero",
    description="Create a hero with all the information",
    tags=["heroes"],
    response_model=HeroSchema,
    status_code=201,
)
async def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


@app.get(
    "/heroes/",
    summary="Read heroes",
    description="Read all heroes",
    tags=["heroes"],
    response_model=list[HeroSchema],
    status_code=200,
)
async def read_heroes(session: Session = Depends(get_session)):
    return session.exec(select(Hero)).all()


@app.get(
    "/heroes/{hero_id}",
    summary="Read a hero",
    description="Read a hero by ID",
    tags=["heroes"],
    response_model=HeroSchema,
    status_code=200,
)
async def read_hero(hero_id: int, session: Session = Depends(get_session)):
    statement = select(Hero).where(Hero.id == hero_id)
    return session.exec(statement).one()


@app.put(
    "/heroes/{hero_id}",
    summary="Update a hero",
    description="Update a hero by ID",
    tags=["heroes"],
    response_model=Hero,
    status_code=200,
)
async def update_hero(hero_id: int, hero_data: Hero, session: Session = Depends(get_session)):
    db_hero = session.get(Hero, hero_id)

    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    for key, value in hero_data.model_dump(exclude_unset=True).items():
        setattr(db_hero, key, value)

    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@app.delete(
    "/heroes/{hero_id}",
    summary="Delete a hero",
    description="Delete a hero by ID",
    tags=["heroes"],
    status_code=204,
)
async def delete_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)

    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    session.delete(hero)
    session.commit()
    return


@app.post(
    "/teams/",
    summary="Create a team",
    description="Create a team with a name",
    tags=["teams"],
    response_model=Team,
    status_code=201,
)
async def create_team(team: Team, session: Session = Depends(get_session)):
    session.add(team)
    session.commit()
    session.refresh(team)
    return team


@app.get(
    "/teams/{team_id}",
    summary="Read team",
    description="Read a team by ID",
    tags=["teams"],
    response_model=Team,
    status_code=200,
)
async def read_team(team_id: int, session: Session = Depends(get_session)):
    team = session.get(Team, team_id)

    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    return team


@app.post(
    "/missions/",
    summary="Create a mission",
    description="Create a mission with a name and description",
    tags=["missions"],
    response_model=Mission,
    status_code=201,
)
async def create_mission(mission: Mission, session: Session = Depends(get_session)):
    session.add(mission)
    session.commit()
    session.refresh(mission)
    return mission


@app.put(
    "/missions/{mission_id}/heroes/{hero_id}",
    summary="Assign a hero to a mission",
    description="Assign a hero to a mission by ID",
    tags=["missions"],
    response_model=MissionSchema,
    status_code=200,
)
def assign_hero_to_mission(mission_id: int, hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    mission = session.get(Mission, mission_id)
    if not hero or not mission:
        raise HTTPException(status_code=404, detail="Hero or Mission not found")

    mission.heroes.append(hero)
    session.add(mission)
    session.commit()

    session.refresh(mission)
    return mission
