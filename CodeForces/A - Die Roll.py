l=list(map(int,input().split()))
n=6-max(l)+1
if n==2:
    print("1/3")
elif n==1:
    print("1/6")
elif n==3:
    print("1/2")
elif n==4:
    print("2/3")
elif n==5:
    print("5/6")
elif n==6:
    print("1/1")
