# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 11:01:27 2018

@author: kyo
"""

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = { person[i][0]:person[i][1] for i in range(3)}

print(answer)