text=input().strip()
key1=list((input().strip()))
key=list(map(int,key1))
keycopy=key[0:]
key.sort()
n=len(text)//len(key)
d={}
for j in key:
    d[j]=[0]*n
c=0
for j in key:
    if j%2==0:
        for i in range(n):
            d[j][i]=text[c]
            c+=1
    else:
        for o in range(n-1,-1,-1):
            d[j][o]=text[c]
            c+=1

d1={"A":"Z","B":"Y","C":"X","D":"W","E":"V","F":"U","G":"T","H":"S","I":"R","J":"Q","K":"P","L":"O","M":"N","N":"M","O":"L","P":"K","Q":"J","R":"I","S":"H","T":"G","U":"F","V":"E","W":"D","X":"C","Y":"B","Z":"A"}
res=""
for i in range(n):
    for j in keycopy:
        res+=d1[d[j][i]]
print(res)
