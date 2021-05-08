# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:08:04 2021

@author: charm
"""
for i in range(int(input())):
    n=int(input())
    result=mod=div=0
    mod=n%4
    div=n//4
    if(n>4):
        betn_layer=16*(div-1)#top most 4 4 4 4 of 1 row gets subracted since 60 is of subtracted 1's in it
        result=(div*60)-betn_layer
        if(mod==1):
            result+=20
        elif(mod==2):
            result+=36
        elif(mod==3):
            result+=51
        result=result-(4*mod)
    else:
        if(mod==0):
            result=60
        elif(mod==1):
            result=20
        elif(mod==2):
            result=36
        elif(mod==3):
            result=51
    print(result)
        
        
    
        
        