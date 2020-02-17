for i in range(int(input())):
    s1=input().strip()
    s2=input().strip()
    s3=input().strip()
    if s1[0]=="l" and s2[0]=="l" and s2[1]=="l":
        print("yes")
    elif s1[1]=="l" and s2[1]=="l" and s2[2]=="l":
        print("yes")
    elif s2[0]=="l" and s3[0]=="l" and s3[1]=="l":
        print("yes")
    elif s2[1]=="l" and s3[1]=="l" and s3[2]=="l":
        print("yes")
    else:
        print("no")
