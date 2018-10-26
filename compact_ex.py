# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:59:47 2018

@author: kyo
"""
co=[0,1,2,"",[], False, {}, None, "All done"]

def compact(lst):
    result=[]
    for i in lst:
        if i:
            result.append(i)
    return result

print(compact(co))

def compact2(l):
    return [val for val in l if val]