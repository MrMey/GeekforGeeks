# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:04:13 2017

@author: Mr_Mey
http://practice.geeksforgeeks.org/problems/equal-to-product/0/?ref=self
"""

t = int(input())
v = []
w = []

for i in range(t):
    v.append(input())
    w.append(input())

for i in range(t):
    arr = []
    prod = int(v[i].split(' ')[1])
    for ind in w[i].split(' '):
        if int(ind) < prod:
            arr += [int(ind)]
    arr.sort()

    
    