import math
h,l=map(int,input().split())
ang=math.atan(l/h)
ang1=math.radians(90)-ang
myang=ang-ang1
A=l*math.tan(myang)
print(A)
