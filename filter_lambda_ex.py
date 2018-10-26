# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:38:39 2018

@author: kyo
"""

users=[{'a':'kyo','t':[]},{'a':'oyo','t':['hi']}]
iu=list(filter(lambda a: a.get('t')==[],users))
au=list(filter(lambda a: a['t'],users))
print(iu)
print(au)