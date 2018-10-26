# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:06:50 2018

@author: kyo
"""

def fib_gen(num):
    a=0
    b=1
    count=0
    while count<num:
        yield b
        a,b=b,a+b
        count+=1


for n in fib_gen(300) :
    print(n)
    
