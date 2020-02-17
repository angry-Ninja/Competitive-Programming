def atom(n,k,m,count):
    if n>m:
        return count-1
    elif n==m:
        return count
    else:
        return atom(n*k,k,m,count+1)

for i in range(int(input())):
    l=list(map(int,input().split()))
    kk=atom(l[0],l[1],l[2],0)
    if kk<0:
        print(0)
    else:
        print(kk)
