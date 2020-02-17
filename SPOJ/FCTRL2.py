for i in range(int(input())):
    a=int(input())
    fact=1
    for i in range(2,a+1):
        fact*=i
    print(fact)
