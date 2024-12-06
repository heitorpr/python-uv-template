from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.domain.services import HeroesService, MissionsService, TeamsService

from .db import get_session
from .services import get_heroes_service, get_missions_service, get_teams_service

SessionDep = Annotated[Session, Depends(get_session)]
HeroesServiceDep = Annotated[HeroesService, Depends(get_heroes_service)]
TeamsServiceDep = Annotated[TeamsService, Depends(get_teams_service)]
MissionsServiceDep = Annotated[MissionsService, Depends(get_missions_service)]
