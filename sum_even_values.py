# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:32:46 2018

@author: kyo
"""

def sum_even_values(*num) :
    return sum(even for even in num if even%2==0)