from collections import Counter
t=int(input())
for k in range(t):
    if k!=0:
        print()
        g=input()
    l=[]
    n=int(input())
    for m in range(n):
        l.append(input().strip())
    d=dict(Counter(l))
    dd=list(d.keys())
    
    nn=[]
    for h in dd:
        b=h[0:2]+h[3:11]+h[12:16]+h[17:21]+h[22:26]+h[27:31]
        nn.append(int(b))
    nn.sort()
    
    for j in nn:
        o=str(j)
        o="0"*(26-len(o))+o
       
        oo=str(o[0:2])+" "+str(o[2:10])+" "+str(o[10:14])+" "+str(o[14:18])+" "+str(o[18:22])+" "+str(o[22:26])
        print(oo,d[oo])
