#!/usr/bin/env python3
""" This module contains the function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """ Returns the sum of the list """
    return sum(input_list)
