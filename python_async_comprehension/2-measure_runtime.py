#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
import random
from typing import Generator, List


async_generator = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the runtime """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_generator() for i in range(4)))
    return asyncio.get_event_loop().time() - start
