from asyncio import sleep

from fastapi import APIRouter

from app.extensions import instrumentator
from app.utils import normally_distributed_jitter

router = APIRouter()


@logarithmic_histogram_generator(
    "router_fast_request_duration",
    start_bucket=0,
    end_bucket=1,
    total_buckets=20,
    additional_labels={"vegetable": "potato"},
)
@router.get("/fast")
async def fast():
    sleep(normally_distributed_jitter(0.01))
    return {"endpoint": "fast"}


@logarithmic_histogram_generator(
    "router_slow_request_duration",
    start_bucket=0,
    end_bucket=1,
    total_buckets=20,
    additional_labels={"vegetable": "cabbage"},
)
@router.get("/slow")
async def slow():
    sleep(normally_distributed_jitter(1))
    return {"endpoint": "slow"}
