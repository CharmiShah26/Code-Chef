# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 23:22:07 2021

@author: charm
"""

n=int(input())
a=list(map(int,input().strip().split()))[:n]
even=odd=0
for i in a:
    if(i%2==0):
        even+=1
    else:
        odd+=1
if(even>odd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")