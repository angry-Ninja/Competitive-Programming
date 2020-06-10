for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    lrev=0
    for j in l:
        if j>k:
            lrev+=(j-k)
    print(lrev)
