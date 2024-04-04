import math
import random


def normally_distributed_jitter(time: float, sd_range: int = 1) -> float:
    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)
    jitter = math.sqrt(-sd_range * math.log(u1)) * math.cos(sd_range * math.pi * u2)
    rescaled_jitter = (time / 10) * jitter
    return time + rescaled_jitter
