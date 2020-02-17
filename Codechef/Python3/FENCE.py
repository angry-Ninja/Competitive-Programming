for i in range(int(input())):
    r,c,plants=list(map(int,input().split()))
    k={}
    edges=0
    for j in range(plants):
        g=list(input().split())
        ss=(g[0]+" "+g[1])
        k[ss]=1
    for x in k:
        #cellsOnBoundry
        x=list(map(int,x.split()))
        peechecell=[x[0],x[1]-1]
        peechecell=" ".join(str(y) for y in peechecell)
        aagecell=[x[0],x[1]+1]
        aagecell=" ".join(str(y) for y in aagecell)
        uparcell=[x[0]-1,x[1]]
        uparcell=" ".join(str(y) for y in uparcell)
        neechecell=[x[0]+1,x[1]]
        neechecell=" ".join(str(y) for y in neechecell)
        try:
            if k[peechecell] ==1:
                pass
        except Exception as e:
            edges+=1
        try:
            if k[aagecell] ==1:
                pass
        except Exception as e:
            edges+=1
        try:
            if k[neechecell] ==1:
                pass
        except Exception as e:
            edges+=1
        try:
            if k[uparcell] ==1:
                pass
        except Exception as e:
            edges+=1
       
    print(edges)
            
        
