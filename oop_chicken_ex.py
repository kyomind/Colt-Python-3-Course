# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:52:43 2018

@author: kyo
"""

class Chicken:
    total_eggs=0
    def __init__(self,name,species) :
        self.name=name
        self.species=species
        self.eggs=0
    
    def lay_egg(self) :
        Chicken.total_eggs+=1
        self.eggs+=1
    
one=Chicken('kyo','fly')
two=Chicken('mary','land')
one.lay_egg()
print(Chicken.total_eggs)
print(one.eggs)
two.lay_egg()
print(Chicken.total_eggs)
print(one.eggs)