#!/usr/bin/env python3
""" A module that defines an async coroutine that runs multiple coroutines"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    A function that runs tha wait_delay function n times using async
    Args:
        n(int): the number of times wait_random will be run
        max_delay: the maximum delay for each wait_random run
    Returns:
        A list of all delays
    """

    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays


if __name__ == "__main__":
    asyncio.run(main())
