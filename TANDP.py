# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:52:56 2021

@author: charm
"""

    
for _ in range(int(input())):
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    thief=(n-x)+(m-y)
    police=(n-a)+(m-b)-min(n-a,m-b)
    if(thief<=police):
        print("YES")
    else:
        print("NO")
    