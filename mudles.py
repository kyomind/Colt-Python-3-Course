# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 11:03:34 2018

@author: kyo
"""
help(list)
class Comment():
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes