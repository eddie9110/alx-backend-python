#!/usr/bin/env python3
"""module contains sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated function takes a list input_list of
    floats as argument and returns their sum as a float"""
    sum = 0
    for element in input_list:
        sum += element
    return sum
