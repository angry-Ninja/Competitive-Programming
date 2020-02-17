def correct(l):
    b1=False
    b2=False
    for j in range(0,3):
        if l[0][j]<=l[1][j] and l[1][j]<=l[2][j]:
            if l[0][j]<l[1][j] :
                b1=True
            if l[1][j]<l[2][j]:
                b2=True
        else:
            return [False, False]
    if b1==b2 and b1==True:
        return [True , True]
    else:
        return [True, False]
    
for j in range(int(input())):
    l=[]
    for g in range(0,3):
        l.append(list(map(int,input().split())))
    a,b,c=l[0],l[1],l[2]
    ans=correct([a,b,c])
    if ans[0] and ans[1]:
        print("yes")
        continue
    ans=correct([a,c,b])
    if ans[0] and ans[1]:
        print("yes")
        continue
    ans=correct([b,c,a])
    if ans[0] and ans[1]:
        print("yes")
        continue
    ans=correct([b,a,c])
    if ans[0] and ans[1]:
        print("yes")
        continue
    ans=correct([c,b,a])
    if ans[0] and ans[1]:
        print("yes")
        continue
    ans=correct([c,a,b])
    if ans[0] and ans[1]:
        print("yes")
        continue
    
    print("no")
        

        
        
