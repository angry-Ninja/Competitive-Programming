import math
def prime(a):
    c=0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            c=1
            break
    if c==1:
        return False
    else:
        return True
def divisors(b):
    d=[]
    for i in range(2,10):
        if i>=b:
            break
        if b%i==0:
            d.append(i)
    return(d)            
n=int(input())
if prime(n):
    print(n)
    print(" ".join(x for x in ["1"]*n))
else:
    div=divisors(n)
    try:
        jj=int(n//max(div))
        print(jj)
        print(" ".join(str(x) for x in [int(max(div))]*jj))
    except Exception as e:
        print(n)
        print(" ".join(x for x in ["1"]*n))
