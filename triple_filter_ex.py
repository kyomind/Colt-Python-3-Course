# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:59:40 2018

@author: kyo
"""

'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(lst):
    return list(map(lambda i: i*3,filter(lambda x: x%4==0,lst)))

print(triple_and_filter([6,8,10,12]))