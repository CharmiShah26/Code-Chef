# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:00:06 2021

@author: charm
"""

for _ in range(int(input())):
    x,y,xr,yr,D=map(int,input().split())
    food=x//xr
    water=y//yr
    if(min(food,water)>=D):
        print("YES")
    else:
        print("NO")