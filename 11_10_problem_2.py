# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:50:39 2017

@author: Mr_Mey
"""

t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()
    if(s1==s2):
        print(0)
    elif(len(s1) != len(s2)):
        print(0)
    else:
        ind = []
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                ind.append(i)
            if len(ind)>2:
                print(0)
                break
        if(len(ind) <2):
            print(0)
        elif (s1[ind[0]]==s2[ind[1]]) & (s1[ind[1]]==s2[ind[0]]):
            print(1)
        else:
            print(0)