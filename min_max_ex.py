# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:06:11 2018

@author: kyo
"""

def extremes(it) :
    mn = min(i for i in it)
    mx = max(i for i in it)
    return (mn,mx)


def extremes1(nums):
    return(min(nums), max(nums))