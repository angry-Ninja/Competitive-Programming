def indexDict(l):
    d={}
    length=0
    i=0
    for j in l:
             # list,length,sum,pos
        try:
            d[j][0].append(i)
            d[j][1]+=1
            d[j][2]+=i
        except:
            d[j]=[[],0,0,0]
        i+=1
    return d

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    xor=[]
    xor1=arr[0]
    for j in range(1,n):
        xor1=xor1^arr[j]
        xor.append(xor1)
        if xor1==0:
            ans+=j
    xors=[arr[0]]+xor
    d=indexDict(xors)
   # print(xors)
   # print(d)
    for i in range(0,n):
        mul=xors[i]
        ind=d[mul]
        if ind[1]>0:
            ans+=ind[2]-ind[1]*(i+1)
            d[mul][1]-=1
            d[mul][2]-=d[mul][0][d[mul][3]]
            d[mul][3]+=1
        
    print(ans)
