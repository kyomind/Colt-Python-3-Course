# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 11:19:52 2018

@author: kyo
"""

donations = dict(sam=25.0, lena=88.99, 
                 chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

print(donations.values())
x=0
for i in donations.values():
    x+=i
print(x)