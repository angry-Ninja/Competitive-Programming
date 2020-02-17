from collections import Counter
n,m=list(map(int,input().split()))
citywon=[] #city=index and value =winner
l=[]
for j in range(m):
    kk=list(map(int,input().split()))
    citywon.append(kk.index(max(kk))+1)
d=dict(Counter(citywon))
res=[]
maxx=max(list(d.values()))
for i in d:
    if d[i]==maxx:
        res.append(i)
print(min(res))
