from collections import Counter
for j in range(int(input())):
    n,q=map(int,input().split())
    s=input()
    fre=dict(Counter(s))
    d=fre.values()
    for i in range(q):
        centers=int(input())
        ans=0
        for k in d:
            if k>centers:
                ans+=k-centers
        print(ans)
