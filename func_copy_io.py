# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:02:39 2018

@author: kyo
"""

def copy(file,copy):
    with open(file) as f:
        data=f.read()
        
    with open(copy,'w') as c:
        c.write(data)
        
copy('lol.txt','copylol.txt')