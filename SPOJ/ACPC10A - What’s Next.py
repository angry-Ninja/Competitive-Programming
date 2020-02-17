x,y,z=list(map(int,input().split()))
while x!=0 or y!=0 or z!=0:
    if z-y==y-x:
        print("AP",z-y+z)
    else:
        print("GP",int((z)*(z/y)))
    x,y,z=list(map(int,input().split()))
