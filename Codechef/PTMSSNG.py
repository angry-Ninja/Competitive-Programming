for _ in range(int(input())):
    n=int(input())
    kk=(4*n)-1
    dx={}
    dy={}
    for j in range(kk):
        l=list(map(int,input().split()))
        try:
            dx[l[0]]+=1
        except:
            dx[l[0]]=1
        try:
            dy[l[1]]+=1
        except:
            dy[l[1]]=1
    x=0
    y=0

    for key in dx.keys():
        if dx[key]%2!=0:
            x=key
            break
    for key in dy.keys():
        if dy[key]%2!=0:
            y=key
            break
    print(x,y)
