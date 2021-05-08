
#approach-charmi
pos=[]
for t in range(int(input())):
    n,k=map(int,input().split())
    s=str(input())
    if(len(s)==n):
        #counter=0
        if("*" not in s):
            print("NO")
        else:
            for i in range(len(s)):
                if(s[i]=="*"):
                    pos.append(i)
            for j in pos:
                counter=0
                for i in range(k):
                    if((i+j)>=n):
                        break
                    elif(s[j+i]=="*"):
                        counter+=1
                if(counter==k):
                    print("YES")
                    break
            if(counter!=k):
                print("NO")
#approach-aryan
 '''
 for i in range(int(input())):
	N,K=map(int,input().split(" "))
	S=input()
	flag=0
	for i in range(N):
		if(S[i]=='*'):
			flag=flag+1
		elif(S[i]!='*'):
			if(flag<K):
			 flag=0
	if(flag>=K):
		print('yes')
	else:
		print('no')
'''               