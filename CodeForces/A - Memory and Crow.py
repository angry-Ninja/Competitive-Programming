n=int(input())
l=list(map(int,input().split()))
sums=[0]
for i in range(n-2,-1,-1):
    g=(l[i+1]-sums[-1])
    l[i]=l[i]+g
    sums.append(g)
for i in l:
    print(i,end=" ")
