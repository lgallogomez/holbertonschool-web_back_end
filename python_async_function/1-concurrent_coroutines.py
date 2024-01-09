#!/usr/bin/env python3

'''
programs contains a coroutine
'''

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    uses wait_rando n times
    '''
    delays_list = []
    all_tasks = [wait_random(max_delay) for i in range(n)]
    # list comprehension doesnt start the function
    for one_task in asyncio.as_completed(all_tasks):
        # starts all wait_random iterations at same time concurrently
        one_delayed_time = await one_task
        delays_list.append(one_delayed_time)
    return delays_list
