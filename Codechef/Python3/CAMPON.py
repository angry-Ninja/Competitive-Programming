for i in range(int(input())):
    prob=[0]*32
    jdecided=int(input())
    for kk in range(jdecided):
        s=list(map(int,input().split()))
        prob[s[0]]=s[1]
    q=int(input())
    for hh in range(q):
        s=list(map(int,input().split()))
        ll=prob[0:s[0]+1]
        if sum(ll)>=s[1]:
            print("Go Camp")
        else:
            print("Go Sleep")
