#!/usr/bin/env python3

'''
coroutine collects 10 rand numbers using the async
comprehensing over async_generator that returns
10 rand nums
'''

async_generator = __import__('0-async_generator').async_generator
import asyncio

async def async_comprehension():
    numbers = [i async for i in async_generator()]
    return numbers
