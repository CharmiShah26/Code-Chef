# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:09:14 2021

@author: charm
"""
t=int(input())
for i in range(t):
    H,x,y,C= map(int, input().split())
    cons_of_singlehh=x+(y//2)
    cons_of_allhh=cons_of_singlehh*H
    if(cons_of_allhh<=C):
        print("Yes")
    else:
        print("No")
    
    
        