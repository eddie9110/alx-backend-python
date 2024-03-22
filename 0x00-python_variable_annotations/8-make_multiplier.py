#!/usr/bin/env python3
"""
  type annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return is a function that multiplies a float by multiplier"""
    def func(arg_: float) -> float:
        return multiplier * arg_
    return func
