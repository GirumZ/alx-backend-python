#!/usr/bin/python3
""" A module that defines an async function called wait_random"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    A function that sleeps for a random float value between 1 and max_delay
    Args:
        max_delay(int): A maximum float value to sleep
    Returns:
        The delay
    """

    delay = random.uniform(1, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    asyncio.run(main())
