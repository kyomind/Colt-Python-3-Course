# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:04:56 2018

@author: kyo
"""

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

def yes_or_no1():
    answer = "yes"
    while True:
        yield answer
        if answer == "yes" :
            answer = "no"
        else:
            answer = "yes"
