# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:06:47 2018

@author: kyo
"""
import csv
with open('ptt.csv','w') as ptt:
    pttcsv= csv.writer(ptt)
    pttcsv.writerow(['hah','hhihi'])
    pttcsv.writerow(['hah','hhihi'])
    for i in range(100):
        pttcsv.writerow(['times',i])
        pttcsv.writerow(['hah','hhihi'])