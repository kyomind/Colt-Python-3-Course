# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:49:31 2018

@author: kyo
"""

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
d={list1[i]:list2[i] for i in range(3)}
print(d)