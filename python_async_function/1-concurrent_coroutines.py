#!/usr/bin/env python3

'''
programs contains a coroutine
'''

wait_random = __import__('0-basic_async_syntax').wait_random

import asyncio
import random
from typing import List

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    does n times 
    '''
    i = 0
    my_list = []
    for i in range(n):
        delay_time = random.uniform(0, max_delay)
        await asyncio.sleep(delay_time)
        my_list.append(delay_time)
    my_list.sort()
    return my_list
