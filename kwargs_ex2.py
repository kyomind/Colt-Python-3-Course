# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:24:32 2018

@author: kyo
"""

'''
calculate(make_float=False, operation='add', 
message='You just added', first=2, second=4) 
# "You just added 6"
calculate(make_float=True, operation='divide', 
first=3.5, second=5) 
# "The result is 0.7"
'''

def calculate(**ones):
    if not 'message' in ones:
        if ones['make_float'] :
            if ones['operation']=='add' :
                return 'The result is '+str(float(ones['first']+ones['second']))
            elif ones['operation']=='subtract' :
                return 'The result is '+str(float(ones['first']-ones['second']))
            elif ones['operation']=='multiply' :
                return 'The result is '+str(float(ones['first']*ones['second']))
            elif ones['operation']=='divide' :
                return 'The result is '+str(float(ones['first']/ones['second']))
        elif ones['make_float']==False :
            if ones['operation']=='add' :
                return 'The result is '+str(int(ones['first']+ones['second']))
            elif ones['operation']=='subtract' :
                return 'The result is '+str(int(ones['first']-ones['second']))
            elif ones['operation']=='multiply' :
                return 'The result is '+str(int(ones['first']*ones['second']))
            elif ones['operation']=='divide' :
                return 'The result is '+str(int(ones['first']/ones['second']))
    elif 'message' in ones:
        if ones['make_float'] :
            if ones['operation']=='add' :
                return ones['message'] +' '+str(float(ones['first']+ones['second']))
            elif ones['operation']=='subtract' :
                return ones['message'] +' '+str(float(ones['first']-ones['second']))
            elif ones['operation']=='multiply' :
                return ones['message'] +' '+str(float(ones['first']*ones['second']))
            elif ones['operation']=='divide' :
                return ones['message'] +' '+str(float(ones['first']/ones['second']))
        elif ones['make_float']==False :
            if ones['operation']=='add' :
                return ones['message'] +' '+str(int(ones['first']+ones['second']))
            elif ones['operation']=='subtract' :
                return ones['message'] +' '+str(int(ones['first']-ones['second']))
            elif ones['operation']=='multiply' :
                return ones['message'] +' '+str(int(ones['first']*ones['second']))
            elif ones['operation']=='divide' :
                return ones['message'] +' '+str(int(ones['first']/ones['second']))
            
# 解答簡潔很多，首先它在函數內先設了一個字典…
def calculate1(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

               
