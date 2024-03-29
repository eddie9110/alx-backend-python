#!/usr/bin/env python3
"""
  type annotation basics
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
