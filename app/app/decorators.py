import logging
from functools import wraps

import numpy as np
from prometheus_client import Histogram

from app.extensions import instrumentator


log = logging.getLogger(__name__)


def logarithmic_buckets(start, end, num_buckets):
    start += 1
    end += 1
    log_start = np.log10(start)
    log_end = np.log10(end)
    log_scale = np.linspace(log_start, log_end, num_buckets + 1)

    # Convert logarithmic scale back to linear scale
    linear_scale = np.power(10, log_scale)

    # Rescale back to 0.
    return [round(x - 1, 3) for x in linear_scale]


def logarithmic_histogram_generator(
    *,
    metric_name: str,
    start_bucket: float,
    end_bucket: float,
    total_buckets: int,
    additional_labels: dict[str, str]
):
    buckets = logarithmic_buckets(start_bucket, end_bucket, total_buckets)
    histogram = Histogram(
        metric_name,
        buckets=buckets,
        labelnames=additional_labels.keys(),
        _labelvalues=additional_labels.values(),
    )

    def decorator(func):
        start_time = time.perf_counter()

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Add your decorator logic here
            return func(*args, **kwargs)

        request_time = time.perf_counter() - start_time
        logger.debug("Request duration %r", request_time)

        return wrapper

    return decorator
