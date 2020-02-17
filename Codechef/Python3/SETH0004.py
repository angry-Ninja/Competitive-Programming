n=int(input())
l=list(map(int,input().split()))
l.sort()
count=0
for j in range(0,len(l)):
    if l[j]!=0:
        count+=1
        for m in range(j+1,len(l)):
            if l[m]%l[j]==0:
                l[m]=0
        l[j]=0
print(count)
