for i in range(0,int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=list(map(int,input().split()))
    gd=[]
    for j in range(1,len(a)-1):
        totalattack=a[j-1]+a[j+1]
        if totalattack<d[j]:
            gd.append(d[j])
    if a[n-1]+a[1]<d[0]:
        gd.append(d[0])

    if a[n-2]+a[0]<d[n-1]:
        gd.append(d[n-1])   

    if len(gd)>0:
        print(max(gd))
    else:
        print(-1)
     
