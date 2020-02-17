N=int(input())
j=1
ans=0
while j*j<=N:
    ans+=((N-j**2)//j)+1
    j+=1
print(ans)
