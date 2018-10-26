# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:16:51 2018

@author: kyo
"""
nums=(2,'hi','a','b')
def is_all_strings(it) :
    return  all(type(i)==str for i in it)
print(is_all_strings(nums))