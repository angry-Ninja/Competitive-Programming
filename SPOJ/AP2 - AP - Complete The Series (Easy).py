for j in range(int(input())):
    f,s,summ=map(int,input().split())
    constant=f+s
    n=(summ)/constant
    if n==int(n):
        n=n*2
    else:
        n=int((int(n)*2)+1)
    print(int(n))
    d=int((s-f)//(n-5))
    a=int(f-2*d)
    for k in range(int(n)):
        print(a, end=" ")
        a=a+d
