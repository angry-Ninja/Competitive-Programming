n=int(input())
while n!=0:
    l=list(map(int,input().split()))
    inv=[0]*n
    for j in range(0,n):
        value=l[j]
        inv[value-1]=j+1
    if l==inv:
        print("ambiguous")
    else:
        print("not ambiguous")
    n=int(input())
