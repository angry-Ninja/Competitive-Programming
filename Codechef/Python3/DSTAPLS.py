for i in range(int(input())):
    n,k=map(int,input().split())
    r=n//k
    if r==k:
        print("NO")
    elif r<k:
        print("YES")
    else:
        if r%k==0:
            print("NO")
        else:
            print("YES")
