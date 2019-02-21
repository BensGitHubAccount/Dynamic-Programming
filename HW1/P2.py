# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:05:59 2019

@author: Benjamin Craver
"""

weights = [7, 3, 8, 4]
values = [12, 5, 10, 6]
capacity = 20
choices = [0,0,0,0]

item = 4
def pack(item, size, amount, util):
    item = item-1
    if item<0:
        table.append([util, *amount, size])
        return 0
    else:
        num = 0
        while size>=num*weights[item]:
            pack(item, size-num*weights[item], amount + [num], util + num*values[item])
            num+=1

table = []
pack(item, capacity, [], 0)

import numpy as np
np.array(table)
best = np.argmax(table,axis=0)[0]

print('The max value occurs when item 1 = {}, item 2 = {}, item 3 = {}, item 4 = {} '.format( *table[best][1:-1][::-1]))
print('with a value of ' + str(table[best][0]))
print('and excess penalty of ' + str(table[best][-1]))