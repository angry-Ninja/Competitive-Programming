n=int(input())
l=list(map(int,input().split()))
a=list(set(l))
k=[]
for i in range(n-1,-1,-1):
    if l[i] in a:
        k.append(l[i])
        a.remove(l[i])
print(len(k))
for i in range(len(k)-1,-1,-1) :
    print(k[i],end=" ")
