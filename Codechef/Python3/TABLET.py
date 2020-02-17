for k in range(int(input())):
    tablets,budget=list(map(int,input().split()))
    area=0
    for h in range(tablets):
        w,h,p=list(map(int,input().split()))
        if p<=budget and (w*h)>area:
            area=w*h
    if area>0:
        print(area)
    else:
        print("no tablet")
