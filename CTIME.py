# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:00:50 2021

@author: charm
"""

def merge(intervals):
        intervals.sort()
        prev = intervals[0]
        res = [prev]
        for i in intervals[1:]:
            # if i is in the prev, e.g., [2,3] is in [1,4], continue without operation
            if i[1] <= prev[1]:
                continue
            # if i and prev overlap, e.g., [1,3] and [2,4], change i[0] = prev[0] and pop out prev
            elif i[0] <= prev[1]:
                i[0] = prev[0]
                res.pop()
            # append the new i
            res.append(i)
            # update prev as i
            prev = i
        return res
for _ in range(int(input())):
    n,k,f=map(int,input().split())
    arr=[]
    total=0
    for i in range(0,n):
        l=[]
        a,b=map(int,input().split())
        l.append(a)
        l.append(b)
        arr.append(l)
    ans=merge(arr)
    for q in ans:
        total=total+q[1]-q[0]
    if(k<=f-total):
        print("yes")
    else:
        print("no")