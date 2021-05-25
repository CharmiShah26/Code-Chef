"""
import math
for _ in range(int(input())):
    k=int(input())
    k1=[]
    add=0
    maxi=2*k+1
    for i in range(1,maxi+1):
        k1.append(k+(i**2))
       # print("i=",i)
        #print("k1 is ",k1)
        if(i>1):
            add+=math.gcd(k1[i-1],k1[i-2])
            #print("add is ",add)
    #print(k1)
    print(add)
    k1.clear()

for i in range(maxi-1):
        add+=math.gcd(k1[i],k1[i+1])

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
 """
import math as m   
for _ in range(int(input())):
    k=int(input())
    k1=[]
    add=0
    maxi=2*k+1
    for i in range(1,maxi):
        add+=m.gcd(k+i*i,k+(i+1)*(i+1))
    print(add)
    k1.clear()      
        