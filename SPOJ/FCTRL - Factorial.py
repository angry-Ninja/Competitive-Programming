for _ in range(int(input())):
    m=5
    num=int(input())
    count=0
    while m<=num:
        count+=num//m
        m=m*5
    print(count)
        
