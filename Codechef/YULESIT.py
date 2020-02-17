from collections import Counter
for j in range(int(input())):
    n=int(input())
    l=list(input().split())
    d=dict(Counter(l))
    for k in d.keys():
        if d[k]==1:
            print(int(k))
            break
