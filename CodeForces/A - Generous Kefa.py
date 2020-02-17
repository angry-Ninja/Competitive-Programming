from collections import Counter
n,f=list(map(int,input().split()))
s=input()
d=dict(Counter(s))
mm=max(list(d.values()))
if mm<=f:
    print("YES")
else:
    print("NO")
