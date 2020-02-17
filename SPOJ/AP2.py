for i in range(int(input())):
    a,b,s=list(map(int,input().split()))
    n=(2*s)//(a+b)
    print(n)
    d=(b-a)//(n-5)
    a1=a-2*d
    print(a1,end=" ")
    for j in range(n-1):
        a1=a1+d
        print(a1,end=" ")
    print()
