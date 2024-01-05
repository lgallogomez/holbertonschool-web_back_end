#!/usr/bin/env python3

'''
programs contains a coroutine
'''

import asyncio
import random


async def wait_random(max_delay = 10):
    '''
    waits for random delay between 0 & max delay
    and returns it
    '''
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
