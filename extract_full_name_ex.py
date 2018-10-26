# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:08:50 2018

@author: kyo
"""

'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
def extract_full_name(lst):
    return list(map(lambda x: x['first']+' '+x['last'] ,lst))

print(extract_full_name(names))