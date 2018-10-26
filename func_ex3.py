# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:49:35 2018

@author: kyo
"""

def speak(a='dog') :
    if a =='dog' :
        return 'woof'
    elif a == 'cat' :
        return 'meow'
    elif a =='pig' :
        return 'oink'
    elif a== 'duck' :
        return 'quack'
    return '?'

def speak2(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"