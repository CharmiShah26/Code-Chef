# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:10:54 2021

@author: charm
"""

t=int(input())
for i in range(t):
    test=0
    n=int(input())
    if(n==1 or n==0):
        print("no\n")
    else:
        for j in range(2,n):
            if n%j==0:
                print('no\n')
                test+=1
                break
        if (test==0):
            print('yes\n')
        