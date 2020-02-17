for j in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    count=0
    modd=k%7
    for m in l:
        if (m%7+modd)%7==0:
            count+=1
    print(count)
