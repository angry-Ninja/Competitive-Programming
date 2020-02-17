n,m=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
j=list(set(l1).intersection(set(l2)))
if len(j)>0:
    print(min(j))
else:
    a1=min(l1)
    a2=min(l2)
    if a1>a2:
        print((a2*10)+a1)
    else:
        print((a1*10)+a2)
