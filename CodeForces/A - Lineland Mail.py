n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    maxx=0
    minn=0
    if i!=0 and i!=n-1:
        peeche=abs(l[i]-l[i-1])
        aage=abs(l[i]-l[i+1])
        peeche1=abs(l[i]-l[0])
        aage1=abs(l[i]-l[-1])
        minn=min(peeche,aage)
        maxx=max(peeche1,aage1)
    if i==0:
        minn=abs(l[0]-l[1])
        maxx=abs(l[0]-l[-1])
    elif i==n-1:
        minn=abs(l[i]-l[i-1])
        maxx=abs(l[i]-l[0])
    print(minn,maxx)
    
