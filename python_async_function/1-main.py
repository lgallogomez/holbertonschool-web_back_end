#!/usr/bin/env python3

'''
Test file for printing the correct output of the wait_n coroutine
'''

import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(7,2)))
#print(asyncio.run(wait_n(10, 7)))
