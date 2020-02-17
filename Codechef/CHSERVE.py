t=int(input())
for i in range(0,t):
    l=input().split()
    a=int(l[0])
    b=int(l[1])
    k=int(l[2])
    p=(a+b)//k
    if p%2==0:
        print("CHEF")
    else:
        print("COOK")
