for i in range(0,int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    sum1=sum(l)
    print(sum1-n+1)
