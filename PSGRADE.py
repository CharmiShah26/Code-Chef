# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 09:23:43 2021

@author: charm
"""

for t in range(int(input())):
    Am,Bm,Cm,Tm,A,B,C=map(int,input().split())
    Cum_Sc=A+B+C
    if(A>=Am and B>=Bm and C>=Cm and Cum_Sc>=Tm):
        print("Yes")
    else:
        print("No")