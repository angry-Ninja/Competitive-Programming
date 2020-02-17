n=int(input())
l=list(map(int,input().split()))
luc=0
unluc=0
for j in l:
    if j%2==0:
        luc+=1
    else:
        unluc+=1
if luc>unluc:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
