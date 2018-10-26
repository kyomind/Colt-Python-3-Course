# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:12:35 2018

@author: kyo
"""

import csv

tone=open('1024.csv',encoding='utf8',newline='')
lst=csv.reader(tone)
lst=list(lst)

one=[]
for i in lst:
    for k in i:
        if '/' in k:
            one.extend(k.split('/')) # 更直觀的做法
#            one.append(k[:k.index('/')])
#            one.append(k[k.index('/')+1:])
        else:
            one.append(k)

def show_me_the_hrs(lst):
    learning_type=('lx','gt','py','en','dk')
    total=0
    for k in range(len(learning_type)):
        onehr=lst.count(learning_type[k])
        twohr=(lst.count(learning_type[k]+'2'))*2
        threehr=(lst.count(learning_type[k]+'3'))*3
        sumhr=onehr+twohr+threehr
        total+=sumhr
        if sumhr:
            print(f'{learning_type[k]} is {sumhr}')
    print(f'Total {total}')

show_me_the_hrs(one)



