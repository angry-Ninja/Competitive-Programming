for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d1=-1
    d2=-1
    Small=99
    for j in range(n-1,0,-1):
        if l[j]>l[j-1]:
            d1=j-1
            break
    if d1!=-1:
        for k in range(d1+1,n):
            if l[d1]<l[k]:
                if Small>l[k]:
                    d2=k
                    Small=l[k]
        l[d1],l[d2]=l[d2],l[d1]

        kk=l[d1+1:]
        kk.sort()
        s=""
        for k in range(d1+1):
            s=s+str(l[k])
        for p in kk:
            s=s+str(p)
        print(s)
    else:
        print(-1)
        
