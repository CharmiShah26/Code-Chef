# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:00:51 2021

@author: charm
"""
#this is not proper approach refer of aryan or from codechef submission which was modified by aryan 

for t in range(int(input())):
    n,r=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ten_f=[]
    #a_diff=list(abs(j-i) for i, j in zip(a[:-1], a[1:]))
    for i in range(1,n):
        a_diff=a[i]-a[i-1]
        #print("a_diff:",a_diff)
        ten_r=b[i-1]+b[i]-(a_diff*r)
        #print("ten_r:",ten_r)
        if(ten_r<0):
            ten_r=0
        ten_f.append(ten_r)
    print(max(ten_f))
    

    
    """
    import numpy as np
    a_np=np.array(a)
    #diff_a=np.diff(a_np)
    diff_sum_a=np.sum(np.diff(a_np))
    ten_red=diff_sum_a*r
    b_np=np.array(b)
    b_sum=np.sum(b_np)
    print(b_sum-ten_red)
else:
    print(b[0])
    
    
    if(n>1):
    a_diff=list(abs(j-i) for i, j in zip(a[:-1], a[1:]))
    sum_a_diff=sum(a_diff)
    sum_b=sum(b)
    tension_r=sum_a_diff*r
    print(sum_b-tension_r)
else:
    print(b[0])

"""