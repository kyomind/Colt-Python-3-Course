# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:07:45 2018

@author: kyo
"""
print('今天跑幾公里')
kms=input('請輸入一個數字：')
miles=float(kms)/1.60934  #這裡一定要先強轉因為input進來的都是字串
print('你今天跑了'+kms+'公里')
print('相當於跑了'+str(miles)+'英里')
print(f'相當於跑了{miles}英里 by F-Strings')
#兩種呈現方式效率高下立見
print(f'相當於跑了{round(miles,2)}英里 by F-Strings + round()')
#上round()，讓輸出不要小數點後那麼多位