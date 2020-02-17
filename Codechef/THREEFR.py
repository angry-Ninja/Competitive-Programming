for l in range(0,int(input())):
    x,y,z=list(map(int,input().split()))
    if x+y-z==0:
        possible=True
    elif x-y+z==0:
        possible=True
    elif -x+y+z==0:
        possible=True
    else :
        possible=False
    if possible:
        print("yes")
    else:
        print("no")
