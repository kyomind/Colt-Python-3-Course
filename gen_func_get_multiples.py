# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:36:14 2018

@author: kyo
"""

def get_multiples(num=1,count=10):
    for i in range(1,count+1):
        res=num*i
        yield res
        
print(list(get_multiples(2,4)))

def get_multiples2(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num