def lcm(x, y):
    from fractions import gcd 
    return x * y // gcd(x, y)

for i in range(0,int(input())):
    n,a,b,k=map(int,input().split())
    lcm1=lcm(a,b)
    ans=(n//a)+(n//b)-2*(n//lcm1)
    if ans>=k:
        print("Win")
    else:
        print("Lose")
