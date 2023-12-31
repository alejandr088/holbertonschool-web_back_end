#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async."""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Execute multiple coroutines at the same time with async."""
    return asyncio.create_task(wait_random(max_delay))
