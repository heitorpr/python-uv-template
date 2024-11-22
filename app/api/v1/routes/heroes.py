from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.api.deps import SessionDep
from app.api.v1.schemas.heroes import HeroSchema
from app.domain.models import Hero

router = APIRouter()


@router.post(
    "/",
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
    "/",
    summary="Read heroes",
    description="Read all heroes",
    tags=["heroes"],
    response_model=list[HeroSchema],
    status_code=200,
)
async def read_heroes(session: SessionDep):
    return session.exec(select(Hero)).all()


@router.get(
    "/{hero_id}",
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
    "/{hero_id}",
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
    "/{hero_id}",
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
