import math
for i in range(0,int(input())):
    a=int(input())
    n=0
    count=0
    while a>1:
        k=int(math.sqrt(a))
        a=a-k*k
        count+=1
    if a==1:
        print(count+1)
    else:
        print(count)
