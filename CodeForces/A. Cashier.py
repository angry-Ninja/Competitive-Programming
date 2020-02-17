cust,tot,bre=list(map(int,input().split()))
breaks=0
for i in range(cust):
    l=list(map(int,input().split()))
    try:
        l[1]=l[0]+l[1]
        breaks=breaks+((l[0]-pre[1])//bre)
    except Exception as e:
        breaks=breaks+(l[0]//bre)
    pre=l[:]
try:
    breaks=breaks+((tot-l[1])//bre)
except Exception as K:
    breaks=tot//bre
print(breaks)
