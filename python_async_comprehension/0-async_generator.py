#!/usr/bin/env python3

import asyncio
import random

'''
corotutine loops 10 times, waits 1 sec, and yield a 
random # between 0 - 10
'''


async def async_generator():
    '''
    creates a values in async context
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
