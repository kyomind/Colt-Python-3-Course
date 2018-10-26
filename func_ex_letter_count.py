# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:04:35 2018

@author: kyo
"""
'''
必須不計大小寫！
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

# the single
def single_letter_count(a,b):
    return a.lower().count(b.lower())

# multiple 要回傳字典，請用字典生成式！
'''
multiple_letter_count("awesome") 
>> {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''
def multiple_letter_count(string):
    return {k:string.count(k) for k in string}