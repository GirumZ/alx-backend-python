#!/usr/bin/env python3
""" A python module that defines a coroutine called async_comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers
    """

    rtn_list = [i async for i in async_generator()]
    return rtn_list
