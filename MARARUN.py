for _ in range(int(input())):
    D,d,A,B,C=map(int,input().strip().split())
    cover=D*d
    if(cover>=10 and cover<21):
        print(A)
    elif(cover>=21 and cover<42):
        print(B)
    elif(cover>=42):
        print(C)
    else:
        print(0)
    