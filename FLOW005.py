# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:17:11 2021

@author: charm
"""

# cook your dish he
notes=[100,50,10,5,2,1]
for i in range(int(input())):
    n=int(input())
    x=0
    for i in notes:
        x+=n//i
        n=n%i
    print(x)
    
   