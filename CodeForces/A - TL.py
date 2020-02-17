ac,wa=list(map(int,input().split()))
AC=list(map(int,input().split()))
WA=list(map(int,input().split()))
AC.sort()
WA.sort()
found=0
for j in range(AC[-1],WA[0]):
    tl=j
    if 2*AC[0]<=tl:
        found=1
        break
if found==1:
    print(tl)
else:
    print(-1)
