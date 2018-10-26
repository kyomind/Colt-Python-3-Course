# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:45:13 2018

@author: kyo
"""

'''
list_manipulation([1,2,3], "remove", "end") # 3
不止要回傳移除值，而且確實要移除該值，讓原lst變成[1,2]
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) 
>>  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30)
>>  [1,2,3,30]
'''
def list_manipulation(lst,act,position,addnum=None):
    if act=='remove' :
        if position=='end' :
            return lst.pop()
        return lst.pop(0)
    else:
        if position=='end' :
            lst.append(addnum)
            return lst
        lst.insert(0,addnum)
        return lst


def list_manipulation1(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection
