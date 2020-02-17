price,dollar,n=list(map(int,input().split()))
tot=((price*((n*(n+1))//2)))
if tot<dollar:
    print(0)
else:
    print(tot-dollar)
