li=input().split(" ")
w=float(li[0])
bal=float(li[1])
if w%5==0 and w<=bal-.50:
    print("%.2f"%(bal-w-.50))
else:
    print("%.2f"%bal)
