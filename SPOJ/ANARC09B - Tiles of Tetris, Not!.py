from math import gcd
a,b=map(int,input().split())
while a!=0 and b!=0:
    print((a*b)//gcd(a,b)**2)
    a,b=map(int,input().split())
