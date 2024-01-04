#!/usr/bin/env python3

'''
program has a single function
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    function returns another function
    '''
    def mult(number: float):
        '''
        function multiplies number times multiplier
        '''
        return (number * multiplier)
    
    return (mult)
