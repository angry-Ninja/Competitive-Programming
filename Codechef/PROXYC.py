for h in range(int(input())):
    l=int(input())
    q=list(input())
    Tneed=(0.75*l)
    has=q.count("P")
    proxy=0
    if Tneed<=has:
        print(0)
    else:
        for j in range(2,(l-2)):
            if q[j]=="A" and (q[j-2]=="P" or q[j-1]=="P") and (q[j+1]=="P" or q[j+2]=="P"):
                proxy+=1
            if proxy+has>=Tneed:
                break
        if proxy+has>=Tneed:
            print(proxy)
        else:
            print(-1)
