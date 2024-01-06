#!/usr/bin/env python3

'''
programs contains a function
'''


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    '''
    creates a task of soing wait_random function
    '''
    return asyncio.create_task(wait_random(max_delay))
    