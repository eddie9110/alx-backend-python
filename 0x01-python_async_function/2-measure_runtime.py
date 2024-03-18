#!/usr/bin/env python3
"""module contains measure_time function """

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int,  max_delay: int) -> float:
    """
    function measures and returns the time taken
    for wait_n(n, max_delay) to execute
    """
    start_ = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_duration = time.time() - start_
    return (time_duration / n)
