# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:03:11 2021

@author: charm
"""

for _ in range(int(input())):
    S=[]
    N,A,B=map(int,input().split())
    game=str('EQUINOX')
    for i in range(N):
        S.append(input())
    Sar=Anu=0
    for j in S:
        if(j[0] in game):
            Sar+=A
        else:
            Anu+=B
    if(Sar>Anu):
        print("SARTHAK")
    elif(Sar<Anu):
        print("ANURADHA")
    else:
        print("DRAW")
    S.clear()