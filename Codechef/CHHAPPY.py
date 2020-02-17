for i in range(0,int(input())):
    n=int(input())
    l=[-9]+list(map(int,input().split()))
    cc=set(range(1,n+1)).intersection(set(l))
    new=[]
    for j in cc:
        new.append(l[j])
    if len(set(new))==len(new):
        print("Poor Chef")
    else:
        print("Truly Happy")
