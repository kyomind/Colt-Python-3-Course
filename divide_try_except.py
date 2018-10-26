# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:21:38 2018

@author: kyo
"""

def divide(num1,num2):
    try:
        total= num1/num2
    except TypeError:
        return 'Please provide two integers or floats'
    except ZeroDivisionError:
        print('Please do not divide by zero')
    return total
   
#def divide(a,b):
#    try:
#        total = a / b
#    except TypeError:
#        return "Please provide two integers or floats"
#    except ZeroDivisionError:
#        return "Please do not divide by zero"
#    return total     