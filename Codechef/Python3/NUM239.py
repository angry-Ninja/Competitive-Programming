for _ in range(int(input())):
    L,R=map(int,input().split())
    count=0
    l1=L%10
    l2=R%10

    for j in range(L,L+1+10-l1):
        if j%10==3 or j%10==2 or j%10==9:
            count+=1
    for j in range(R,R-l2-1,-1):
        if j%10==3 or j%10==2 or j%10==9:
            count+=1      
    L=L+10-l1
    R=R-l2
    count+=3*((R-L)//10)
    print(count)
