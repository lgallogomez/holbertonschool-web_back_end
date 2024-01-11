#!/usr/bin/env python3

'''
programs contains a function
'''


import time
from tracemalloc import start
from typing import List
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measures execution time for wait_n function
    '''
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finished_time = time.perf_counter()
    total_time = finished_time - start_time
    return total_time / n
