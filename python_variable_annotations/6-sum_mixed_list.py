#!/usr/bin/env python3

"""
program has a single function
"""


from typing import List, Union


def sum_mixed_list(input_list: Union[List[float], List[int]]) -> float:
    """
    function adds floats & ints of a list, returns float
    """
    return sum(input_list)
