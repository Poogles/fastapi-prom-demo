import math
import random
from asyncio import sleep


from fastapi import FastAPI
from app.extensions import instrumentator
from app.router import router


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/ping")
    async def ping():
        return "PONG"

    app.include_router(router, prefix="/api")

    instrumentator.instrument(app).expose(app)
    return app
