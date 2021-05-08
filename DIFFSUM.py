# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 21:43:19 2021

@author: charm
"""
#sol 1
list=[]
for i in range(2):
    list.append(int(input()))
x,y=[list[i] for i in (0,1)]
if(x>y):
    print(x-y)
else:
    print(x+y)

#sol2
    x=int(input())
y=int(input())
if(x>y):
    print(x-y)
else:
    print(x+y)