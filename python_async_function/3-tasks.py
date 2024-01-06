#!/usr/bin/env python3

'''
programs contains a function
'''


import time
from tracemalloc import start
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    '''
    creates a task of soing wait_random function
    '''
    task = asyncio.create_task(wait_random())
    return task