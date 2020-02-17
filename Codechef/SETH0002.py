for j in range(int(input())):
    a,b,c=map(int,input().split())
    if a>1 and b>1 and c>1:
        a=a%2
        b=b%2
        c=c%2
        if a==1 and b==1 and c==1:
            print("YES")
        if a==0 and b==0 and c==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
