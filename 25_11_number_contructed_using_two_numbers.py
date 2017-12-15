# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:44:27 2017

@author: Mr_Mey
https://practice.geeksforgeeks.org/problems/count-numbers-which-can-be-constructed-using-two-numbers/0
"""

t = int(input())
v = []
for i in range(t):
    v.append(input())

for i in range(t):
    [x,y,n] = [int(x) for x in v[i].split(' ')]

    
    visited = []
    if x < y:
       if x>n:
           print(0)
       elif y>n:
           print(n//x)
       else:
           count = 0
           cnt_x = 0
           cnt_y = 1
           while cnt_x * x <= n:
               while cnt_x*x+cnt_y*y <= n:
                   if cnt_x*x+cnt_y*y not in visited:
                       count +=1
                       visited.append(cnt_x*x+cnt_y*y)
                   cnt_y += 1
               cnt_y = 0
               cnt_x +=1
           print(count)
    else:
       if y>n:
           print(0)
       elif x>n:
           print(n//y)
       else:
           count = 0
           cnt_x = 0
           cnt_y = 0
           while cnt_y * y <= n:
               while cnt_x*x+cnt_y*y <= n:
                   if cnt_x*x+cnt_y*y not in visited:
                       count +=1
                       visited.append(cnt_x*x+cnt_y*y)
                   cnt_x += 1
               cnt_x = 0
               cnt_y +=1
           print(count)