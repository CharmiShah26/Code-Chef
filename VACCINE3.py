
import math
for _ in range(int(input())):
	age=list(map(int,input().strip().split()))
	P=age[1]
	G=age[0]
	total=sum(age[G+2:])
	mod=total%P#0
	div=total//P#5
	minimum=div+1
	maximum=age[G+1]+mod
	print(minimum,div+math.ceil(maximum/P))
