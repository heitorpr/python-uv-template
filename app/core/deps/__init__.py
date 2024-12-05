from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.core.deps.services import get_heroes_service, get_teams_service
from app.domain.services.heroes import HeroesService
from app.domain.services.teams import TeamsService

from .db import get_session

SessionDep = Annotated[Session, Depends(get_session)]
HeroesServiceDep = Annotated[HeroesService, Depends(get_heroes_service)]
TeamsServiceDep = Annotated[TeamsService, Depends(get_teams_service)]
