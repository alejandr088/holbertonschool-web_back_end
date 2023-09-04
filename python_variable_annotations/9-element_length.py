#!/usr/bin/env python3
""" This module is used to calculate the length"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples containing elements and their length """
    return [(i, len(i)) for i in lst]
