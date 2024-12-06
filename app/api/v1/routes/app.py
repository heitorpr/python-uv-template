from fastapi import APIRouter
from sqlmodel import select

from app.core.deps import SessionDep

router = APIRouter()


@router.get("/")
async def read_root():
    """Root API Operation."""
    return {"status": "ok"}


@router.get("/healthz")
async def healthcheck(session: SessionDep):
    """Healthcheck API Operation."""
    result = (await session.execute(select(1))).first()

    if result is None:
        return {
            "status": "error",
            "message": "No health status found",
        }

    return {"status": "ok"}
