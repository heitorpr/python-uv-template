from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.core.deps.services import get_heroes_service
from app.domain.services.heroes import HeroesService

from .db import get_session

SessionDep = Annotated[Session, Depends(get_session)]
HeroesServiceDep = Annotated[HeroesService, Depends(get_heroes_service)]
