# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:02:01 2018

@author: kyo
"""

def interleave(str1,str2) :
    aa=zip([i for i in str1] ,[i for i in str2])
    b=''
    for i in aa:
        b+=''.join(i)
    return b  

def interleave1(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))