for j in range(int(input())):
    n=int(input())
    l=list(
        (map(int,input().split())))
    sums=[]
    s=0
    length=len(l)
    for j in range(length-1,0,-1):
        s+=l[j]
        sums.append(s)
    ans=0
    ll=length-1
    r=-1
    for k in range(length-1):
        ans+=abs((l[k]*ll)-sums[r])
        ll-=1
        r-=1
    print(ans)
