import math
n=int(input())
l=[1]
p=int(math.sqrt(n)+1)
for i in range(2,p):
    if n%i==0:
        if n/i==i:
            l.append(i)
        else:
            l.append(i)
            l.append(n/i)

if sum(l)==n and n!=1:
    print("Perfect")
else:
    print("Not Perfect")
