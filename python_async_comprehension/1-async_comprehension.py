#!/usr/bin/env python3

'''
coroutine collects 10 rand numbers using the async
comprehensing over async_generator that returns
10 rand nums
'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    calls function async_generator, iterates in async mode
    the number of times the func is programmed, returns a
    list with rand numbers.
    '''
    numbers = [i async for i in async_generator()]
    return numbers
