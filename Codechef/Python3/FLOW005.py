for i in range(int(input())):
    s=int(input())
    notes=0
    for j in [100,50,10,5,2,1]:
        notes+=s//j
        s=s%j
    print(notes)
