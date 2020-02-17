for i in range(0,int(input())):
    n,m,k=list(map(int,input().split()))
    c=0
    count=0
    while n>=m:
        if (n%m)==0:
            print(count)
            c=1
            break
        else:
            n=n-k
            count+=1
    if c==0:
        print(-1)
