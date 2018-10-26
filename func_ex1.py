# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:35:23 2018

@author: kyo
"""

#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    lst=[]
    for i in range(1,50) :
        if i%2==0:
            lst.append(i)
    return lst
print(generate_evens())
