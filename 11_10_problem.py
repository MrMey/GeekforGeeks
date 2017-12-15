# -*- coding: utf-8 -*-

"""
@author: Mr_Mey
code for problem:
Count of strings that can be formed using a, b and c under given constraints 
"""

t = int(input())

for i in range(t):
    n = int(input())
    #case when n = 1,2,3 treated separetly
    if n == 1:
        print(3)
    elif n == 2:
        print(5)
    elif n == 3:
        print(19)
    else:
        print(n*(n-1)*(n-2)/2+3/2*n*(n-1)+2*n+1)
