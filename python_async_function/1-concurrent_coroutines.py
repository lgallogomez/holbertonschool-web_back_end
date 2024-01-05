#!/usr/bin/env python3

'''
programs contains a coroutine
'''


from hmac import new
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    uses wait_rando n times
    '''
    my_list = []
    for i in range(n):
        delay_time = await wait_random(max_delay)
        new_value = delay_time
        if not my_list:
            my_list.append(new_value)
        for element in my_list:
            if new_value < element:
                my_list.insert(my_list.index(delay_time), new_value)
            else:
                my_list.insert(my_list.index(element) + 1, new_value)
    return my_list
