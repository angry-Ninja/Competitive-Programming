for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    half=n/2
    summ=sum(l)
    if k<half:
        sonn=sum(l[:k])
        fath=summ-sonn
    else:
        fath=sum(l[n-k:])
        sonn=summ-fath
        
    print(abs(fath-sonn))
        
