import logging

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api.v1 import api_router as api_v1_router
from src.core.settings import settings

# Logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

app = FastAPI(default_response_class=ORJSONResponse)


app.include_router(api_v1_router, prefix=settings.api_v1_str)
