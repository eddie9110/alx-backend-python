#!/usr/bin/env python3

"""
module contains function async_comprehension

"""


import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    function performs an asynchronous comprehension.

    Return: list of floats generated
    
    """
    result = [i async for i in async_generator()]
    return result
