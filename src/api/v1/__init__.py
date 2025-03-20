from fastapi import APIRouter

from .routes import app, heroes, missions, teams

api_router = APIRouter()
api_router.include_router(missions.router, prefix="/missions")
api_router.include_router(heroes.router, prefix="/heroes")
api_router.include_router(teams.router, prefix="/teams")
api_router.include_router(app.router, tags=["health"])
