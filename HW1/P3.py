# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:16:10 2019

@author: Benjamin Craver
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([('A',1,{'weight':9}),('A',2,{'weight':8})])
G.add_edges_from([(1,3,{'weight':7}),(1,4,{'weight':3}),(1,5,{'weight':4})])
G.add_edges_from([(2,3,{'weight':4}),(2,4,{'weight':3}),(2,5,{'weight':6})])
G.add_edges_from([(3,6,{'weight':5}),(3,7,{'weight':8})])
G.add_edges_from([(4,6,{'weight':10}),(4,7,{'weight':8})])
G.add_edges_from([(5,6,{'weight':4}),(5,7,{'weight':5})])
G.add_edges_from([(6,'B',{'weight':6}),(7,'B',{'weight':4})])
G.number_of_edges()
G.number_of_nodes()

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

table = []
def path(source, target, trace, cost):
    if source == target:
        table.append([cost, *trace])
    else:
        for n in G.neighbors(source):
            path(n,target, trace + [n], cost + G.get_edge_data(source,n)['weight'])
        

path('A','B', ['A'], 0)
import numpy as np
np.array(table)
shortest_path = np.argmin(table,axis=0)[0]

print('The shortest path is: ' + str(table[shortest_path][1:]))
print('with a cost of ' + str(table[shortest_path][0]))