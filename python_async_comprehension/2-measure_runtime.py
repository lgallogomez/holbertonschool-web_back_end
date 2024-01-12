#!/usr/bin/env python3

'''
module executes async_comprehension function 4 times
and calculates time elapsed during execution
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    async function executes async_comprehension function 4 times
    and calculates time elapsed during execution
    '''
    tasks = [async_comprehension() for i in range(4)]
    start_time = time.time()
    result = await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
