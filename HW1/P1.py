# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:05:59 2019

@author: Benjamin Craver
"""

demand = [4, 1, 3, 2][::-1]
cum_demand = [sum(demand[0:d+1]) for d,i in enumerate(demand)]
# can ignore pair cost because amount sold is fixed
# pair_cost = 7 
setup_cost = 40
holding_cost = 10



def find(month, demand, stock, cost, output):
    month = month-1
    if month< 0:
        table.append([cost, *output, stock])
        return 0
    else:
        if demand[month] <= stock:
            find(month, demand, stock - demand[month], cost + 10*(demand[month] - stock), output + [0])
        else:
            for p in range(1,11):
                if demand[month] <= stock + p:
                    find(month, demand, stock + p - demand[month], cost - 40 + 10*(demand[month] - stock - p), output + [p])
    
table = []
month = 4
find(month, demand, 0, 0, [])


import numpy as np
np.array(table)
best = np.argmax(table,axis=0)[0]

print('The min cost occurs when production of month 1 = {}, month 2 = {}, month 3 = {}, month 4 = {}'.format(*table[best][1:-1]))
print('with a value of ' + str(table[best][0]))
print('and excess of ' + str(table[best][-1]))

