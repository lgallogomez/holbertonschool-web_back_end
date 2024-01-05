#!/usr/bin/env python3

'''
programs contains a coroutine
'''


from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    uses wait_rando n times
    '''
    delays_list = []
    idx = 0
    for i in range(n):
        delay_time = await wait_random(max_delay)
        while idx < len(delays_list) and delay_time > delays_list[idx]:
            idx += 1
        delays_list.insert(idx, delay_time)
    return delays_list
