for i in range(int(input())):
    l=list(map(int,input().split()))
    mm=max(l)
    for j in range(l.count(mm)):
        l.remove(mm)
    try:
        print(max(l))
    except Exception as e:
        print(mm)
    
