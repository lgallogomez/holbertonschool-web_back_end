#!/usr/bin/env python3

'''
programs contains a coroutine
'''


from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    uses wait_rando n times
    '''
    my_list = []
    for i in range(n):
        delay_time = await wait_random(max_delay)
        my_list.append(delay_time)
    return my_list
