n,x,y=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,n):
	day=l[i]
	p=i-x
	if p<0:
		p=0
	li1=l[p:i]
	k=i+y+1
	if k>n:
		k=n
	li2=l[i+1:k]
	li1.append(9999999999)
	li2.append(9999999999)
	if min(li1)>day and min(li2)>day:
		break
print(l.index(day)+1)
