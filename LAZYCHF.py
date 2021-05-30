# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:06:57 2021

@author: charm
"""

for _ in range(int(input())):
    x,m,d=map(int,input().strip().split())
    result=min(x*m,x+d)
    print(result)