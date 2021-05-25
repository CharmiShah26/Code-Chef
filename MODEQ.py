for i in range(int(input())):
	n,m= map(int,input().split())
	ans=0
	list = [1 for i in range(n+1)]
	for a in range(2,n+1):
		mod1=m%a
		ans=ans+list[mod1];
		for b in range(mod1,n+1,a):
			list[b]=list[b]+1
	print(ans)

"""
for _ in range(int(input())):
    n,m=map(int,input().split())
    flag=0
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            print("a=",a,", b=",b)
            if ((m%a)%b)==((m%b)%a):
                print("|__________________ YES")
                flag+=1
    print(flag)  
    
CHECK THIS ONCE 

for _ in range(int(input())):
    n,m=map(int,input().split())
    count=0
    a=1
    while(a!=n):
        for i in range(a+1,n+1):
            b=i
            #print("a=",a,", b=",b)
            if(b%a==0 or (m%a==0 and m%b==0)):
                #print("|__________________ YES")
                count+=1
        a+=1
    print(count)

m%a and  m%b is zero than count that (a,b)
if m%a is zero and a%b is zero than count tHat pair
"""
    
            
            
