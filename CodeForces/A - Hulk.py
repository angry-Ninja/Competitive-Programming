n=int(input())
h="I hate "
l="I love "
s=""
for i in range(1,n+1):
    if i==1:
        s=s+h
    elif i%2==0:
        s+="that "+l
    else:
        s+="that "+h
print(s+"it")
