def fib(n):
    if n<=0:
        return 0
    elif lookup[n]==None:
        if n==1 or n==2:
            lookup[n]=1
        else:
            lookup[n]=2*fib(n-2)+fib(n-1)
    
    return lookup[n]

l=list(map(int,input().split()))
ll=l[1: len(l)]
c=0
for i in ll:
    lookup=[None]*(i+1)
    lookup[0]=0
    print(fib(i),end=" ")
    if c!=l[0]-1:
        c+=1
        print(2**i,end=" ")
    else:
        print(2**i)
