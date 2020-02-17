t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    while y>0:
        t=y
        y=x%y
        x=t
    print(x*2)  
