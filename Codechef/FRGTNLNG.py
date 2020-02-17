for i in range(0,int(input())):
    n,k=list(map(int,input().split()))
    old=input().split()
    neww=[]
    ke=[]
    for p in range(0,k):
        neww+=list(set(input().split()))
    for h in old:
        if h in neww:
            ke.append("YES")
        else:
            ke.append("NO")
    ss=" ".join(ke)
    print(ss)
