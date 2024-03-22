#!/usr/bin/env python3
"""
  module contains to_kv function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function converts a string and int/float to tuple"""
    return (k, float(v**2))
