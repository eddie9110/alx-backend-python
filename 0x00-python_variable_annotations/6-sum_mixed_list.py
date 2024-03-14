#!/usr/bin/env python3
"""module contains function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function takes a list mxd_lst of integers
    and floats and returns their sum as a float."""
    sum = 0
    for element in mxd_lst:
        sum += element
    return sum
