for i in range(0,int(input())):
    poemL,pagesleft,money,Cshowed=list(map(int,input().split()))
    pages=[]
    price=[]
    for j in range(0,Cshowed):
        h=list(map(int,input().split()))
        pages.append(h[0])
        price.append(h[1])
    pagesneeded=poemL-pagesleft
    c=0
    for k in range(0,Cshowed):
        if pages[k]>=pagesneeded and price[k]<=money:
            c=1
            break
    if c==0:
        print("UnluckyChef")
    else:
        print("LuckyChef")
