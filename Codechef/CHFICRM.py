for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    shop={"five":0,"ten":0,"fif":0}
    count=0
    for j in l:
        if j==5:
            shop["five"]+=1
            count+=1
        elif j ==10 and shop["five"]>0:
            shop["ten"]+=1
            shop["five"]-=1
            count+=1
        elif j ==15:
            if shop["ten"]>0 :
                shop["fif"]+=1
                shop["ten"]-=1
                count+=1
            elif shop["five"]>1:
                shop["fif"]+=1
                shop["five"]-=2
                count+=1                
            else:
                break
        else:
            break
    if count==n:
        print("YES")
    else:
        print("NO")
