d={}
for i in range(3):
    l=list(map(int,input().split()))
    for j in range(3):
        k=str(i)+" "+str(j)
        d[k]=l[j]%2
g={"0 0":1,"0 1":1,"0 2":1,"1 0":1,"1 1":1,"1 2":1,"2 0":1,"2 1":1,"2 2":1}
for x in d:
    aa=x
    if d[x]==1:
        x=list(map(int,x.split()))
        peechecell=[x[0],x[1]-1]
        peechecell=" ".join(str(y) for y in peechecell)
        aagecell=[x[0],x[1]+1]
        aagecell=" ".join(str(y) for y in aagecell)
        uparcell=[x[0]-1,x[1]]
        uparcell=" ".join(str(y) for y in uparcell)
        neechecell=[x[0]+1,x[1]]
        neechecell=" ".join(str(y) for y in neechecell)
        if g[aa]==1:
            g[aa]=0
        else:
            g[aa]=1
        try:
            if g[peechecell] ==1:
                g[peechecell]=0
            else:
                g[peechecell]=1
        except Exception as e:
            pass
        try:
            if g[aagecell] ==1:
                g[aagecell]=0
            else:
                g[aagecell]=1
        except Exception as e:
            pass
        try:
            if g[neechecell] ==1:
                g[neechecell]=0
            else:
                g[neechecell]=1
        except Exception as e:
            pass
        try:
            if g[uparcell] ==1:
                g[uparcell]=0
            else:
                g[uparcell]=1
        except Exception as e:
            pass
ii=list(g.values())
for i in range(0,9,3):
    s=str(ii[i])+str(ii[i+1])+str(ii[i+2])
    print(s)
