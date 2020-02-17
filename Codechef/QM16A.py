for _ in range(int(input())):
    s1=set(input().split())
    s2=set(input().split())
    s3=s1.intersection(s2)
    if len(s3)>0:
        print("Yes")
    else:
        print("No")
