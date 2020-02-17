for i in range(0,int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(l.index(min(l))+1)
