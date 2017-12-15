# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 17:36:46 2017

@author: Mr_Mey
"""

import math

def s(x):
    x = str(x)
    result = 0
    for i in x:
        result += int(i)
    return(result)

t = int(input())

for i in range(t):
    n = int(input())
    if n == 1:
        print(-1)
    else:        
        x = int(math.sqrt(n/2))
        print(x)
        while x*x < n:
            if x * (x + s(x)) == n:
                print(x)
                break
                break
            else:
                x += 1
        if x*x>=n:
            print(-1)


