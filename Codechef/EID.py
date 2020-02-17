for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ll=list(set(l))
    lll=[]
    if len(ll)!=n:
        print(0)
    else:
        ll.sort(reverse=True)
        for j in range(0,n-1):
            lll.append(ll[j]-ll[j+1])
        print(min(lll))
