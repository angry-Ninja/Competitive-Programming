count=0
for j in range(int(input())):
    p,q=list(map(int,input().split()))
    if q-p>=2:
        count+=1
print(count)
