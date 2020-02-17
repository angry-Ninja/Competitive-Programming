a=input()
b=input()
c=str(int(a)+int(b))
a1=""
b1=""
c1=""
for s in a:
    if s!='0':
        a1+=s
for s in b:
    if s!='0':
        b1+=s
for s in c:
    if s!='0':
        c1+=s

if int(a1)+int(b1)==int(c1):
    print("YES")
else:
    print("NO")
