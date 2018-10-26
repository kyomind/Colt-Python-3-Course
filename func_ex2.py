# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:02:39 2018

@author: kyo
"""

def yell(string) :
    return string.upper()+'!'

def yell2(word):
    return "{}!".format(word.upper())

def yell3(word):
    return f"{word.upper()}!"