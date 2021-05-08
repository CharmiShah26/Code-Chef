# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:17:58 2021

@author: charm
"""
def gcd(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
def lcm(x,y):
    return int(x*y/gcd(x,y))
    """
    if x>y:
        greater=x
    else:
        greater=y
    if(x%greater==0 and y%greater==0):
        return greater
    greater=greater+1
    """
for t in range(int(input())):
    a,b=map(int,input().split())
    print(str(gcd(a,b))+" "+str(lcm(a,b)))
    
    
    '''
    easiest approach
    
    import math
    for _ in range(int(input())):
    a,b=map(int,input().split())
    gcd=math.gcd(a,b)
    lcm=a*b//gcd
    print(gcd,lcm)
    
    '''
    