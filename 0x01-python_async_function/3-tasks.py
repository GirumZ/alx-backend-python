#!/usr/bin/env python3
""" A python module that defines the task_wait_random function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ A function that returns an async.Task"""
    task = asyncio.Task(wait_random(max_delay))
    return task
