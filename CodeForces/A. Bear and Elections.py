n=int(input())
l1=list(map(int,input().split()))
l=[]
candy=0
for i in range(1,n):
    if l1[i]>=l1[0]:
        l.append(l1[i])
if len(l)>=1:
    mm=max(l)
    while mm>=l1[0]:
        candy+=1
        l[l.index(mm)]=mm-1
        l1[0]=l1[0]+1
        mm=max(l)
print(candy)
