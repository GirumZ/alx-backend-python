#!/usr/bin/env python3
""" A python modul definig a function that calculates run time"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measures the run time of wait_n
    Args:
        n(int): the number of times wait_random will be run
        max_delay: the maximum delay for each wait_random run
    Returns:
        list[float]: A list of all delays
    """

    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    duration = perf_counter() - start
    return duration / n
