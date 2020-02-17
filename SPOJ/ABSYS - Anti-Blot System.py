for j in range(int(input())):
    input()
    inp=input().split("+")
    first=inp[0].strip()
    inp2=(inp[1]).split("=")
    second=inp2[0].strip()
    third=inp2[1].strip()
    findA,findB,findC=([False]*3)
    try:
        first=int(first)
    except:
        findA=True
    try:
        second=int(second)
    except:
        findB=True
    try:
        third=int(third)
    except:
        findC=True
    
    if findA:
        first=third-second
    elif findB:
        second=third-first
    else:
        third=first+second
    print(first,"+",second,"=",third)
    
