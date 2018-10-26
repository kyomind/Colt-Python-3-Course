# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:41:39 2018

@author: kyo
"""

def sum_floats(*num):
    return sum(f for f in num if type(f)==float)