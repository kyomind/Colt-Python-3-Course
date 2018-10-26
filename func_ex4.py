# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:04:30 2018

@author: kyo
"""

def return_day(p):
    days={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",
         6:"Friday",7:"Saturday"}
    if days.get(p) :
        return days.get(p)
    return 'None'


def return_day1(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None