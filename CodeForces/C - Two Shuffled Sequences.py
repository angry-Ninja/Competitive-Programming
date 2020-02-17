from collections import Counter
n=int(input())
l=list(map(int,input().split()))
d=dict(Counter(l))
val=list(d.values())
if max(val)>2:
    print("NO")
else:
    print("YES")
    kk=[]
    for h in d.keys():
        if d[h]==2:
            kk.append(h)      
    kk.sort()
    jj=list(d.keys())
    jj=list(set(jj))
    jj.sort(reverse=True)
    print(len(kk))
    print(" ".join(str(x) for x in kk))
    print(len(jj))
    print(" ".join(str(x) for x in jj))
