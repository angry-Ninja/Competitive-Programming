for i in range(0,int(input())):
    E,C=list(map(int,input().split()))
    A=sum(list(map(int,input().split())))
    if A<=C:
        print("Yes")
    else:
        print("No")
