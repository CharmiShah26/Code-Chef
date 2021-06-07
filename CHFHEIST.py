"""
O(n) appraoch
for _ in range(int(input())):
    D,d,p,q=map(int,input().strip().split())
    count=p*d
    i=d
    while(i<D):
        current=p+q*(i//d)
        #print("current:",current)
        count+=current
        #print("count:",count)
        #print(i)
        i=i+1
    print(count)
    
    
    """
def totalamount_even(n,D,d,p,q):
    S=0
    S=d*n//2*(2*p+(n-1)*q)
    S+=(D%d)*(p+n*q)
    return S
def totalamount_odd(n,D,d,p,q):
    S=0
    S=d*(n*(p+(n-1)//2)*q)
    S+=(D%d)*(p+n*q)
    return S
for _ in range(int(input())):
    D,d,p,q=map(int,input().strip().split())
    n=D//d
    if(n%2==0):
        print(totalamount_even(n,D,d,p,q))   
    else:
        print(totalamount_odd(n,D,d,p,q))
                        
                        