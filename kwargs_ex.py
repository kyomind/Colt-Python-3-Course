# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:08:11 2018

@author: kyo
"""

def combine_words(word,**words) :
    for k in words :
        if k=='prefix' :
            return words[k]+word
        elif k=='suffix' :
#        else: >> 錯誤寫法，一定要elif
            return word+words[k]
    return word

def combine_words1(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word