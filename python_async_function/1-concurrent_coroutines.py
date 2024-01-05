#!/usr/bin/env python3

'''
programs contains a coroutine
'''


import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    does n times
    '''
    my_list = []
    for i in range(n):
        delay_time = random.uniform(0, max_delay)
        await asyncio.sleep(delay_time)
        my_list.append(delay_time)
    my_list.sort()
    return my_list
