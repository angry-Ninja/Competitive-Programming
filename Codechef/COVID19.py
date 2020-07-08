for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=[]
    c=1
    for j in range(1,n):
        if abs(l[j]-l[j-1])<3:
            c+=1
        else:
            ans.append(c)
            c=1
    ans.append(c)
    print(min(ans),max(ans))
        
        
