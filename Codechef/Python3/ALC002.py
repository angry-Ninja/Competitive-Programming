for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    while len(l)>=k:
        ele=len(l)//k
        ans1=[]
        if len(l)>k and len(l)%k!=0:
            left=len(l)%k
            ans1=l[-left:]
        start=0
        end=k
        ans=[]
        for j in range(ele):
            e=sum(l[start:end])
            ans.append(e)
            start=end
            end+=k
        l=ans[:]+ans1
    for j in l:
        print(j,end=" ")

