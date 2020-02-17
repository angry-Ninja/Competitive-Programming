for i in range(int(input())):
    n=int(input())
    s,c=input().split()
    cou=s.count(c)
    prevc=0
    l=[]
    for j in range(len(s)):
        if s[j]==c and len(l)==0:
            l.append(j)
            prevc=j
        elif s[j]==c:
            l.append(j-prevc-1)
            prevc=j
    l.append(n-prevc-1)
    k=[]
    summ=0
    for h in l:
        if h not in k:
            summ+=(l.count(h))*((h*(h+1))//2)
            k.append(h)
    tot=(n*(n+1))//2
  
    if cou==0:
        print(0)
    else:
        print(tot-summ)
            
