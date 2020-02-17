from math import sqrt , gcd
def factors(n):
    l=[1]
    for j in range(2,int(sqrt(n))+1):
        if n%j==0:
            if n//j!=j:
                l.append(j)
                l.append(n//j)
            else:
                l.append(j)
    return l
        
a,b=map(int,input().split())
if a==b:
    print(0)
else:
    d=abs(a-b)
    fact=factors(d)
    lcm=[]
    for j in fact:
        lcm1=((a+j)*(b+j))//gcd(a+j,b+j)
        lcm.append(lcm1)
    minn=min(lcm)
    nn=lcm.index(minn)
    print(fact[nn])
