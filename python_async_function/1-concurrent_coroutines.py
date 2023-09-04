#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async."""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """Execute multiple coroutines at the same time with async."""
    delays: List[float] = []
    for a in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
