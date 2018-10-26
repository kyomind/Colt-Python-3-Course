# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:13:37 2018

@author: kyo
"""

def copy_and_reverse(file,copy):
    
    with open(file) as f:
        data=f.read()
        
    with open(copy,'w') as c:
        c.write(data[::-1])

copy_and_reverse('lol.txt','copylol.txt')