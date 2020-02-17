for i in range(0,int(input())):
    H,s,t=list(map(int,input().split()))
    houses=s*t
    occ=[]
    l=list(map(int,input().split()))
    for j in l:
        if j-houses<=0:
          
            occ=occ+list(range(1,j+1))
        else:
        
            occ=occ+list(range(j-houses,j+1))
        if j+houses>100:
           
            occ=occ+list(range(j,101))
        else:
          
            occ=occ+list(range(j,j+houses+1))
    print(100-len(list(set(occ))))
