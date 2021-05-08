# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 09:33:38 2021

@author: charm
"""

for t in range(int(input())):
    n,x=map(int,input().split())
    #method 1 of finding unique elements
    a_list=list(map(int,input().strip().split()))[:n]
    a_set=set(a_list)
    flag=len(a_set)
    diff=n-x
    if(flag==n or flag>diff):
        print(diff)
    elif(flag<=diff):
        print(flag)
        
        
        
   
    #method-2 to find unique elements
#ini=a[0]
#flag=1#initially it's set to one and if different flavor is seen it will get incremented
#for i in a:
#    if(i!=ini):
#        flag+=1
#        ini=i
