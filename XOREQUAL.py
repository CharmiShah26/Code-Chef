# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:05:09 2021

@author: charm
"""


for _ in range(int(input())):
    n=int(input())
    n=n-1
    print(pow(2,n))














"""
for _ in range(int(input())):
    n=int(input())
    print(2**(n-1))
    

    left=right=count=0
    for i in range(2**n):
        print("i=",i)
        left=(i)^(i+1)
        right=(i+2)^(i+3)
        if(left==right):
            count+=1
    if(count>0):
        print(count)
"""