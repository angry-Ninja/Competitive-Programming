n=int(input())
l=list(map(int,input().split()))
odd=[]
even=[]
for j in l:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
odd.sort(reverse=True)
even.sort(reverse=True)
evenL=len(even)
oddL=len(odd)
mm=min(evenL,oddL)

neven=even[mm:evenL]
nodd=odd[mm:oddL]
if len(neven)>len(nodd):
    summ=sum(neven)-neven[0]+sum(nodd)
elif len(neven)<len(nodd):
    summ=sum(neven)-nodd[0]+sum(nodd)
else:
    summ=0
print(summ)
