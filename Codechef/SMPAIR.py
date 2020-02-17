for i in range(0,int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    print(l[0]+l[1])
