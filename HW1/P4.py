# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:39:59 2019

@author: Benjamin Craver
"""
def fxn(x,i):
    if i == 0:
        return 2*x
    if i == 1:
        return x*x 
    if i == 2:
        return x*x 
    print(i)
    
def pen(x,i):
    if i == 0:
        return x*x
    if i == 1:
        return x*x 
    if i == 2:
        return x
    print(i)
    
    
    
def solve(i, total_pen, xs, value):
    i = i-1
    if i < 0:
        table.append([value, *xs, total_pen])
        return 0
    x=0
    while total_pen + pen(x,i) <= 4:
        solve(i, total_pen+pen(x,i), xs+[x], value+fxn(x,i))
        x+=1
    
table = []
solve(3, 0, [], 0)

import numpy as np
np.array(table)
best = np.argmax(table,axis=0)[0]

print('The max value occurs when x1 = {}, x2 = {}, x3 = {}'.format(*table[best][1:-1][::-1]))
print('with a value of ' + str(table[best][0]))
print('and excess penalty of ' + str(table[best][-1]))