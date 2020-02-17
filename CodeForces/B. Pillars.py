n=int(input())
l=list(map(int,input().split()))
i=l.index(max(l))
l1=l[0:i]
l2=l[i+1:n]
if sorted(l1)==l1:
    if sorted(l2,reverse=True)==l2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
