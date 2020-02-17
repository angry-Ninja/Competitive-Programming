for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m1=max(l)
    l.remove(m1)
    m2=max(l)
    l.remove(m2)
    for j in l:
        if j <1:
            l.remove(j)
    k=len(l)
    if k+1<=min(m1,m2):
        print(k)
    else:
        print(min(m1,m2)-1)
