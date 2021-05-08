# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 21:00:18 2021

@author: charm
"""

for _ in range(int(input())):
    L=int(input())
    S=str(input())
    one=0
    zero=0
    flag=0
    for j in range(L):
        if(S[j]=="0"):
            zero+=1
        else:
            one+=1
        if(one>=zero):
            flag=1
            break
    if(flag==0):
        print("No")
    else:
        print("Yes")