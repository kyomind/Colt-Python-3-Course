# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:56:44 2018

@author: kyo
"""

['lx/py']
['lx','py']
aa='lx/py'
aa.index('/')
bb=[]
def spilt(lst) :
    for i in lst :
        if '/' in i :
            bb.append(i[:i.index('/')])
            bb.append(i[i.index('/')+1:])
    print(bb)      