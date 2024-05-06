#!/usr/bin/env python3
"""A module that defines an async coroutine that runs multiple coroutines"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that runs tha wait_delay function n times using async
    Args:
        n(int): the number of times wait_random will be run
        max_delay: the maximum delay for each wait_random run
    Returns:
        list[float]: A list of all delays
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
