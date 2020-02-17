from math import gcd
for i in range(int(input())):
    n,a,k=list(map(int,input().split()))
    s=(n-2)*180
    deno=n*(n-1)
    num=a*deno+(k-1)*((2*s)-(2*a*n))
    if gcd(num,deno)==1:
        print(num,deno)
    else:
        h=gcd(num,deno)
        print((num//h),(deno//h))
    
