# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:36:58 2018
人類VS電腦 對決剪刀石頭布 機器人
@author: kyo
"""
import random
rand_num=random.randint(1,3)
if rand_num==1:
    computer='布'
elif rand_num==2:
    computer='石頭'
else :
    computer='剪刀'
print(computer)