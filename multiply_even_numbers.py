# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:45:30 2018

@author: kyo
"""
'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(lst): 
    result=1
    for i in lst:
        if i%2==0:
            result*=i
    return result
