#!/usr/bin/env python3
"""Basic Async Syntax"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine."""
    random_float = uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
