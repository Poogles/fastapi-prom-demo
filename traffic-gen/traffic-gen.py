import random
import time

import requests

DOMAIN = "http://localhost:8000"


def _make_request(url: str) -> int:
    start_time = time.perf_counter()
    requests.get(DOMAIN + "/" + url).raise_for_status()
    return time.perf_counter() - start_time


if __name__ == "__main__":
    endpoints = ["ping" "api/fast", "api/slow"]

    while True:
        endpoint = random.choice(endpoints)
        duration = _make_request(endpoint)
        print(f"request made to {endpoint}, duration {duration}")
