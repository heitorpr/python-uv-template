#!/usr/bin/env python3

from eralchemy import render_er
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from sqlmodel import SQLModel

from app.api.v1 import api_router as api_v1_router
from app.core.settings import settings

app = FastAPI(default_response_class=ORJSONResponse)


app.include_router(api_v1_router, prefix=settings.api_v1_str)


# Generate the ER diagram

target_metadata = SQLModel.metadata
filename = "app/alembic/db_mer.md"
render_er(target_metadata, filename)
