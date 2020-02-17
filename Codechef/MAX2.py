n=int(input())
s=input()
poww=0
for i in range(n-1,-1,-1):
    if s[i]=="1":
        poww=n-i
        break
if poww!=0:
    print(poww-1)
else:
    print(poww)
