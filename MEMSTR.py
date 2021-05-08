def check(a,b):
	n=len(a)
	m=len(b)
	j=0
	i=0
	while(j < m):
		while(i < n and a[i]!=b[j]):
			i=i+1
		if(i == n):
			return True
		i=i+1
		j=j+1
	return False
	
def conv(n):
	res=""
	while(n):
		a=n%2
		a=str(a)
		ch = '0' + a
		res += ch
		n>>=1
	res=res[::-1]
	return res
def decimalToBinary(n):
	return "{0:b}".format(int(n))


t=int(input())
for i in range(t):
	s=str(input())
	ans="e"
	for j in range((1<<11)+1):
		bin=""
		if(j == 0):
			bin = "0"
		else:
			bin = decimalToBinary(j)
			print('bin=',bin)
		if(check(s, bin)):
			print("in")
			ans = bin
			break
	print(ans)	
	
	