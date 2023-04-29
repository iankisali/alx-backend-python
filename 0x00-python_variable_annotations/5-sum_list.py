#!/usr/bin/env python3
"""type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns sum as float."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returning sum of list"""
    return sum(input_list)
