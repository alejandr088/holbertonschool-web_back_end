#!/usr/bin/env python3
""" This module is used to calculate the length"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
