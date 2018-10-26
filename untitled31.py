# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:19:43 2018

@author: kyo
"""

abc=[('a', 'b'), ('a', 'b'), ('a', 'b')]
#b=''
#for i in abc :
#    a=''.join(i)
#    b+=a
#print(b)
print(''.join(''.join(i) for i in abc))