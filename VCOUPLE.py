# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:19:33 2021

@author: charm
"""


t=int(input())
for i in range(t):
    N=int(input())
    m=0
    b = list(map(int,input().strip().split()))[:N]
    #print(b)
    b.sort(reverse=True)
    #print(b)
    g = list(map(int,input().strip().split()))[:N]
    #print(g)
    for j in range(0,N):
        ele=b[i]+g[i]
        if(ele>m):
            m=ele    
    print(m)    
   
    
    
    
    
    
    """
     np_b=np.array(b)
    sort_b=np.sort(np_b)
    
    for k in range(N):
        g.append(int(input()))
    np_g=np.array(g)
    sort_g=np.sort(np_g)
    print(sort_b(N-1)+sort_g(N-1))"""