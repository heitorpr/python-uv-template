from fastapi import APIRouter

from app.api.v1.schemas import HeroPublic
from app.core.deps import HeroesServiceDep
from app.domain.models.hero import HeroCreate, HeroUpdate

router = APIRouter()


@router.post(
    "/",
    summary="Create a hero",
    description="Create a hero with all the information",
    tags=["heroes"],
    response_model=HeroPublic,
    status_code=201,
)
async def create_hero(hero: HeroCreate, service: HeroesServiceDep):
    return await service.create(hero)


@router.get(
    "/{hero_id}",
    summary="Read a hero",
    description="Read a hero by ID",
    tags=["heroes"],
    response_model=HeroPublic,
    status_code=200,
)
async def read_hero(hero_id: int, service: HeroesServiceDep):
    return await service.get(hero_id)


@router.put(
    "/{hero_id}",
    summary="Update a hero",
    description="Update a hero by ID",
    tags=["heroes"],
    response_model=HeroPublic,
    status_code=200,
)
async def update_hero(hero_id: int, hero_data: HeroUpdate, service: HeroesServiceDep):
    return await service.update(hero_id, hero_data)


@router.delete(
    "/{hero_id}",
    summary="Delete a hero",
    description="Delete a hero by ID",
    tags=["heroes"],
    status_code=204,
)
async def delete_hero(hero_id: int, service: HeroesServiceDep):
    return await service.delete(hero_id)


@router.put(
    "/{hero_id}/assign-team/{team_id}",
    summary="Assign a hero to a team",
    description="Assign a hero to a team by ID",
    tags=["heroes"],
    response_model=HeroPublic,
    status_code=200,
)
async def assign_hero_to_team(hero_id: int, team_id: int, service: HeroesServiceDep):
    return await service.assign_team(hero_id, team_id)
