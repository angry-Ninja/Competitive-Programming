for i in range(int(input())):
    a,l,d=list(map(int,input().split()))
    res=(l-a+d)//d
    print(res)
