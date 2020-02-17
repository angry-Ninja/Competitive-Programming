n,m=list(map(int,input().split()))
nn=[n//5]*5
mm=[m//5]*5
bache1=((n//5)*5)
bache2=(m//5)*5
for i in range(bache1+1,n+1):
    nn[i%5]+=1
for i in range(bache2+1,m+1):
    mm[i%5]+=1
print((nn[0]*mm[0])+(nn[1]*mm[4])+(nn[2]*mm[3])+(nn[4]*mm[1])+(nn[3]*mm[2]))
