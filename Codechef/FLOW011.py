for i in range(int(input())):
    bs=int(input())
    if bs<1500:
        res=((bs*(0.10))+(bs)+(bs*(0.90)))
    else:
        res=500+bs+(0.98*bs)
    
    print('%.2f'%res)
