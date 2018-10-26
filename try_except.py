# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:48:38 2018

@author: kyo
"""

d={'a':1,'b':2,'c':3}

def get(d,key) :
    try:
        d[key]
    except KeyError as kk:
        print(f'{kk} is not ok')
    else:
        print('ok')
    finally:
        print('final')
    