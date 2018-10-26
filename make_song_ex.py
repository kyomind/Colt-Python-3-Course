# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:05:08 2018

@author: kyo
"""

def make_song(num=99,bev='soda'):  
    while num > 0 :
        if num==1:
            yield f'Only 1 bottle of {bev} left!'
        else:
            yield f'{num} bottles of {bev} on the wall.'
        num-=1
    yield f'No more {bev}!'
    raise StopIteration
        
def make_song1(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)