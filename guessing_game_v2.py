# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:35:31 2018

@author: kyo
"""

#import random
#random_num= random.randint(1,10)
#your_num= input('guess a number 1-10: ')
# while your_num=='' :
#    your_num=input('please insert a number: ')
# your_num=int(your_num)
# while True :
#    if random_num==your_num :
#        print(f'yes, you got it !! it\'s {random_num}')
#        break
#    elif random_num > your_num :
#        your_num=int(input('too low, guess another: '))
#    else:
#        your_num=int(input('too high, guess another: '))

import random
random_num = random.randint(1, 10)
your_num = ''
# while your_num=='' :
#    your_num=input('please insert a number: ')
# your_num=int(your_num)
while random_num != your_num:
    your_num = input('please insert a number 1-10: ')
    your_num = int(your_num)
    if random_num == your_num:
        print(f'yes, you got it !! it\'s {random_num}')
        again = input('do you want to play again (y/n): ')
        if again == 'y':  # 其實只有y才會繼續，輸入別的都中止
            random_num = random.randint(1, 10)
            your_num = ''
        else:
            print('thanks for playing')
            break
    elif random_num > your_num:
        print('too low, guess another: ')
    else:
        print('too high, guess another: ')
