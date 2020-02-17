n,q=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(n):
    l3.append(l1[i]*l2[i])
for j in range(q):
    a,b=list(map(int,input().split()))
    a=a-1
    ll=l3[a:b]
    print(sum(ll))
    
