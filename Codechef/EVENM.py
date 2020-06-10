for _ in range(0,int(input())):
    n=int(input())
    count=1
    if n%2==1:
        for j in range(n):
            for j in range(n):
                print(count,end=" ")
                count+=1
            print()
    else:
        s1=""
        for j in range(n):
            for i in range(n):
                s1+=str(count)+" "
                count+=1
            s1.strip()
            if j%2==1:
                l=list(s1.split())
                for p in range(len(l)-1,-1,-1):
                    print(l[p],end=" ")
                print()
            else:
                print(s1)
            s1=""
