#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async."""
import asyncio
import time
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines at the same time with async."""
    delay_list = []
    for i in range(n):
        delay_list.append(await (task_wait_random(max_delay)))
    return sorted(delay_list)
