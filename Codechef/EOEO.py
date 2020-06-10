for _ in range(int(input())):
    n=int(input())
    if n%2==1:
        print((n-1)//2)
    else:
        count=0
        for j in range(100):
            n=n//2
            count+=1
            if n%2==1:
                break
        line=n*2
        print((line-2)//4)
