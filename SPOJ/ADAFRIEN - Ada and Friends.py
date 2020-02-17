Q,K=map(int,input().split())
d={}
for j in range(Q):
    l=input().split()
    try:
        d[l[0]]+=int(l[1])
    except:
        d[l[0]]=int(l[1])
tup=d.items()
l=[]
for k,v in tup:
    l.append((v,k))
sorted_l=sorted(l,reverse=True)
summ=0
for p in range(0,min(K,len(sorted_l))):
    summ+=sorted_l[p][0]
print(summ)

