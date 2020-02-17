for i in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    maxx=0
    for j in range(n):
        maxx=max(2*A[j]-B[j],maxx)
    if maxx<0:
        maxx=0
    print(maxx*10)    
        
