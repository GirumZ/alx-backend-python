#!/usr/bin/env python3
""" A python module that defines a coroutine called measure_runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ A coroutine that measures runtime"""

    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    duration = end - start
    return duration
