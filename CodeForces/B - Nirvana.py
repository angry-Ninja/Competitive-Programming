n=input()
intn=list(map(int,list(n)))
pro=[]
if int(n)>9:
    for i in range(0,len(n)-1):
        ss=""
        tt="".join(v for v in n[0:i+1])
        t=int(tt)-1
        ss+=str(t)+"9"*(len(n)-i-1)
        pro.append(ss)
    pro.append(n)
else:
    pro.append(n)
ans=[]

for j in pro:
    anss=1
    for k in j:
        if j.index(k)==0  and k=='0': 
            pass
        else:
            anss*=int(k)
    ans.append(anss)
print(max(ans))   
