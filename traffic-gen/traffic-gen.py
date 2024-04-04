import random
import time

import requests

DOMAIN = "http://localhost:3000"


def _make_request(url: str) -> int:
    start_time = time.perf_counter()
    requests.get(DOMAIN + "/" + url)
    return time.perf_counter() - start_time


if __name__ == "__main__":
    endpoints = ["fast", "slow"]

    while True:
        endpoint = random.choice(endpoints)
        duration = _make_request(endpoint)
        print(f"request made to {endpoint}, duration {duration}")
