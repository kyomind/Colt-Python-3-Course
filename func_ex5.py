# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:35:49 2018

@author: kyo
"""

def last_element(lst):
    if lst==[]:
        return None
    elif lst[-1]:
        return lst[-1]

def last_element1(l):
    if l:
        return l[-1]
    return None