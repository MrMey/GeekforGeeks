# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:11:25 2017

@author: Mr_Mey
"""

t = int(input())
n=[]

for i in range(t):
    n.append(input())
    
for i in range(t):   
    if n[i] == '1':
        print(0)
    else:
        if n[i][-1] in ['0','2','4','6','8']:
            b = int(n[i]) // 2
            print(b*(int(n[i])-1))
        else:
            b = (int(n[i])-1) // 2
            print(b*int(n[i]))           
    