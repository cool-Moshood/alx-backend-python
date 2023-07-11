#!/usr/bin/env python3
""" an asynchronous coroutine that takes in
two integer argument"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return a list of values in async"""

    sec_list = []
    for _ in range(0, n):
        sec_list.append(wait_random(max_delay))
        srt = await asyncio.gather(*sec_list)
        return sorted(srt)
