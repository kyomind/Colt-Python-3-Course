# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:45:51 2018

@author: kyo
"""

def week() :
    days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    for i in days:
        yield i

        
day=week()