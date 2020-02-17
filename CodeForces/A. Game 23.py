def fact(n):
    count=0
    while n%2==0:
        n=n//2
        count+=1
    while n%3==0:
        n=n//3
        count+=1
    if n==1:
        return count
    else:
        return -1
x,y=list(map(int,input().split()))
if y%x==0:
    ans=y//x
    res=fact(ans)
    if res!=-1:
        print(res)
    else:
        print(-1)
else:
    print(-1)
