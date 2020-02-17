a,b=map(int,input().split())
c=0
for j in range(a,b+1):
    if len(str(j))==len(set(str(j))):
        print(j)
        c=1
        break
if c==0:
    print(-1)
