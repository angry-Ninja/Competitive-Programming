n=int(input())
while n!=-1:
    l=[]
    summ=0
    for j in range(n):
        l.append(int(input()))
        summ+=l[-1]
    if summ%n!=0:
        print(-1)
    else:
        toffee_in_each=summ//n
        shift=0
        for k in l:
            shift+=abs(toffee_in_each-k)

        print(shift//2)
    n=int(input())
