from fastapi import APIRouter

from .routes import hero_association

api_router = APIRouter()
api_router.include_router(
    hero_association.router, prefix="/hero_association", tags=["hero_association"]
)
