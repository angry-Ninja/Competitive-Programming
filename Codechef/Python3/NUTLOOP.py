for i in range(int(input())):
    n=int(input())
    l1=list(input().split())
    l2=list(input().split())
    l3=[]
    for i in range(0,n):
        if int(l1[i]+l2[i])>int(l2[i]+l1[i]):
            l3.append(l1[i]+l2[i])
        else:
            l3.append(l2[i]+l1[i])
    for y in l3:
        print(int(y), end=" ")
    print("")  
