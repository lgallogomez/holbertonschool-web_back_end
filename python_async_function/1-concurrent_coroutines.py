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
    delays_list = []
    insertion_point = 0
    for i in range(n):
        delay_time = await wait_random(max_delay)
        
        while insertion_point < len(delays_list) and delay_time > delays_list[insertion_point]:
            insertion_point += 1
        delays_list.insert(insertion_point, delay_time)
    return delays_list
