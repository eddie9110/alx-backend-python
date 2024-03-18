#!/usr/bin/env python3
"""Module contains task_wait_n function"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): No. of calls
        max_delay: 
    Return: List of delay times
    """
    tasks_ = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks_)]
