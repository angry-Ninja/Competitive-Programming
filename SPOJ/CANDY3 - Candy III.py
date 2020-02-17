for j in range(int(input())):
    input()
    n=int(input())
    summ=0
    for k in range(n):
        summ+=int(input())
    if summ%n==0:
        print("YES")
    else:
        print("NO")
