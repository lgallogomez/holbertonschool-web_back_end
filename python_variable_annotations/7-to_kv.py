#!/usr/bin/env python3


'''
program has a single function
'''


from typing import Tuple, Union



def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    function takes args & returns a Tuple
    '''
    return (k, v)
