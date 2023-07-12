#!/usr/bin/env python3
"""a coroutine called async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator,
    then return the 10 random numbers"""
    numb = [x async for x in async_generator()]
    return numb
