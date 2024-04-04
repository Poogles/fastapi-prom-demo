import math
import random
from asyncio import sleep


from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


def normally_distributed_jitter(time: float, sd_range: int = 1) -> float:
    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)
    jitter = math.sqrt(-sd_range * math.log(u1)) * math.cos(sd_range * math.pi * u2)
    rescaled_jitter = (time / 10) * jitter
    return time + rescaled_jitter


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/slow")
    async def slow():
        sleep(normally_distributed_jitter(1))
        return {"message": "slow"}

    @app.get("/fast")
    async def fast():
        sleep(normally_distributed_jitter(0.01))
        return {"message": "fast"}

    Instrumentator().instrument(app).expose(app)
    return app
