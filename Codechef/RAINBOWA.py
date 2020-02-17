for i in range(0,int(input())):
    n=int(input())
    w=list(map(int,input().split()))
    try:
        ii=w.index(7)
        seven=w.count(7)
        if seven%2==0:
            l1=w[0:ii+(seven//2)]
            l2=w[ii+(seven//2):n]
        else:
            l1=w[0:ii+(seven//2)]
            l2=w[ii+(seven//2)+1:n]
        l2.reverse()
        q=len(l1)
        q2=len(l2)
        c=0
        cou=1
        pp=0
        if q==q2:
            for k in range(0,q):
                jj=l1.count(cou)
                if l1[k]==l2[k]==cou:
                    
                    pp+=1
                    if pp==jj:
                        cou+=1
                        pp=0
                else:
                    c=1
                    break
            if c==0:
                if seven>1 and cou==8:
                    print("yes")
                elif seven==1 and cou==7:
                    print("yes")
                else:
                    print("no")
            else:
                print("no")
        else:
            print("no")
    except Exception as e:
        print("no")
