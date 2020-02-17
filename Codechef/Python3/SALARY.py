for i in range(0,int(input())):
    n=int(input())
    w=list(map(int,input().split()))
    mm=min(w)
    kk=w.count(mm)
    print(sum(w)-n*mm)
