# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 21:44:54 2021

@author: charm
"""
from functools import reduce
def sublist(A):
    B = [[ ]]   
   # first loop  
    for i in range(len(A) + 1):
        for j in range(i + 1, len(A) + 1):
             # slice the subarray  
            sub = A[i:j] 
            B.append(sub) 
    return B[1:]
def bitwiseAND(A):
    B=[]
    for i in A:
        and_of_each_sublist=reduce(lambda x, y: x & y,i)
        #print("i:"+str(i)+"and_sublist:"+str(and_sublist))
        B.append(and_of_each_sublist)
    return B

def bitwiseOR(A):
    or_sublist=reduce(lambda x, y : x | y, A)
    return or_sublist
            
for t in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().strip().split()))[:n]
    sub_list=sublist(a)
    bitwise_AND=bitwiseAND(sub_list)
    print(bitwiseOR(bitwise_AND))
    for i in range(q):
        x,v=map(int,input().split())
        a[x-1]=v
        sub_list=sublist(a)
        bitwise_AND=bitwiseAND(sub_list)
        print(bitwiseOR(bitwise_AND))
            
    