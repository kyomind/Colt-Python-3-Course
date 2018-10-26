# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:19:13 2018

1-20，要顯示x是偶數或奇數，遇到4和13要顯示unlucky

@author: kyo
"""
for i in range(1,
               21):
    #    if i%2==0 and i!=4:
    #        print(f'{i} is even')
    #    elif i%2==1 and i!=13:
    #        print(f'{i} is odd')
    #    else:
    #        print(f'{i} is UNLUCKY!')

    # 更簡潔做法，先找完4和13，下面就不用再另外處理
    #    if i==4 or i==13:
    #        print(f'{i} is UNLUCKY!')
    #    elif i%2==1:
    #        print(f'{i} is odd')
    #    else:
    #        print(f'{i} is even')

    # f-strings 強化法
    if i == 4 or i == 13:
        word = 'UNLUCKY!'
    elif i % 2 == 1:
        word = 'odd'
    else:
        word = 'even'
    print(f'{i} is {word}')
