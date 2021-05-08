# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:07:36 2021

@author: charm
"""
for _ in range(int(input())):
    arr=[]
    result=[]
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    for i in range(n):
        arr.append(input())    
    
    for i in arr:
        P=F=0
        #print("i:",i)
        P=i.count('P')
        #print("P:",P)
        F=i.count('F')
        #print("F:",F)
        if(F>=x or (F==(x-1) and P>=y)):
            result.append(1)
            #print("yes")
        else:
            result.append(0)
            #print("no")
    #print(result)
    print(*result,sep="")
    result.clear()#clearing list
    arr.clear()
            