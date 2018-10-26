# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:16:21 2018

@author: kyo
"""

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
while number!=5:
    number=randint(1,10)
    i+=1
    print(f'第{i}次的數字是{number}')
    if i == 20 :
        print('game over')
        break