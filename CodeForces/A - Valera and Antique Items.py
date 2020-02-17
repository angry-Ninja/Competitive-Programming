n,money=list(map(int,input().split()))
prices=[]
sell=[]
for j in range(n):
    ll=list(map(int,input().split()))
    prices.append(ll[1:])
gg=0
for i in prices:
    gg+=1
    for k in i:
        if k<money:
            sell.append(gg)
            break
seller=list(set(sell))
seller.sort()
print(len(seller))
for h in seller:
    print(h,end=" ")
