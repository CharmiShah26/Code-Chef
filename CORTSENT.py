def check_lower(a):
    leng=len(a)
    #print("leng lower=",leng)
    flag=0
    for i in range(leng):
        #print("lower a[",i,"]=",a[i])
        if(a[i]>='a' and a[i]<='m'):
            flag+=1
       # print("flag lower=",flag)
    if(flag==leng):
        return 1
    else:
        return 0
def check_upper(a):
    leng=len(a)
    #print("leng upper=",leng)
    flag=0
    for i in range(leng):
        #print("upper a[",i,"]=",a[i])
        if(a[i]>='N' and a[i]<='Z'):
            flag+=1
        #print("flag upper=",flag)
    if(flag==leng):
        return 1
    else:
        return 0        
    
for _ in range(int(input())):
    n=list(input().strip().split())
    k=int(n[0])
    n=n[1:]
    count=0
    for i in range(k):
        #print("n[",i,"]=",n[i])
        if(check_lower(n[i]) or check_upper(n[i])):
            count+=1
        else:
            count=0
    if(count==k):
        print("YES")
    else:
        print("NO")
    