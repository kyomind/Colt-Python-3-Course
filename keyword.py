# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:02:03 2018

@author: kyo 
"""

import keyword
def contains_keyword(*lst):
    return any(i for i in lst if keyword.iskeyword(i))

def contains_keyword2(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False