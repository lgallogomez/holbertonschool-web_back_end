#!/usr/bin/env python3

'''
corotutine loops 10 times, waits 1 sec, and yield a 
random # between 0 - 10
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    creates a values in async context
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
