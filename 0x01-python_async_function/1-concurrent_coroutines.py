#!/usr/bin/env python3
"""
module contains wait_n function
"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    args:
        n (int):
        max_delay:
    return: list of all the delays(float)
    """
    lst = []
    for i in range(n):
        lst.append(wait_random(max_delay))
    return [await a for a in asyncio.as_completed(lst)]
