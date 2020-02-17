n=int(input())
b=False
l=[]
for i in range(0,n):
    k=list(input().split())
    if int(k[1])>=2400 and int(k[2])>int(k[1]):
        b=True
if b:
    print("YES")
else:
    print("NO")
