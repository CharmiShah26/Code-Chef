arr=[]
t=int(input())
for i in range(t):
    arr.append(int(input()))
arr.sort()
for i in range(t):
    print(arr[i])