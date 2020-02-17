for h in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    summ=0
    for i in range(0,n//2,1):
        summ+=l[i]-l[n-i-1]
    print(summ)
