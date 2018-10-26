# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:32:11 2018

@author: kyo
"""

with open('lol.txt','r+') as f:
    f.writelines('new')
    f.seek(100)
    f.writelines('newnewn')
         