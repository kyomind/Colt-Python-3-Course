# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:59:00 2018

@author: kyo
"""
# 只能輸入數字版
times = int(input('我跟你說幾次了？'))
# x=0
# while x < times:
#    print('hello加油')
#    x+=1

# 用for+range
for i in range(times):
    print(f'hello加油第{i+1}次')  # 不加1從0開始會有第0次出現
