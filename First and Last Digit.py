# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:15:45 2021

@author: charm
"""

t=int(input())
arr=[]
for i in range(t):
    for j in range(10):
        arr.append(int(input()))
    first=arr[1]
    last=arr[-1]
    print(first+last)
        

    
    
    