# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 11:14:36 2018

@author: kyo
"""

class BankAccount :
    def __init__(self,name):
        self.owner=name
        self.balance=0.0
        
    def deposit(self,addnum) :
        self.balance+=addnum
        return self.balance
    
    def withdraw(self,subnum) :
        self.balance-=subnum
        return self.balance
    
    def seebalance(self) :
        return self.balance
    
    def sayhi(self):
        print('hi')
    
#class BankAccount:
# 
#    def __init__(self, name):
#        self.owner = name
#        self.balance = 0.0
# 
#    def getBalance(self):
#        return self.balance
# 
#    def withdraw(self, amount):
#        self.balance -= amount
#        return self.balance
# 
#    def deposit(self, amount):
#        self.balance += amo unt
#        return self.balance



user1=BankAccount('Darcy')
print(user1.owner)
user1.deposit(100)
user1.withdraw(50)
print(user1.seebalance())
user1.sayhi()
