for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=0
    for j in range(1,n):
        ans+=abs(l[j-1]-l[j])-1
    print(ans)
