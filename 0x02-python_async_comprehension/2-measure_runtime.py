#!/usr/bin/env python3

"""
module contains async function measure_runtime
"""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine measures the runtime of async comprehension

    Return: Runtime
    """
    start = time.time()
    result = await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return (end - start)
