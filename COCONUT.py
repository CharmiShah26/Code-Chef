# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:41:01 2021

@author: charm
"""

for i in range(int(input())):
    x,y,a,b=map(int,input().strip().split())
    water=a//x
    pulp=b//y
    print(water+pulp)