n,x,y=map(int,input().split())
p=input()
k=p[(n-x):]
count=0
h=0
for j in range(len(k)-1,-1,-1):
    if h==y:
        if k[j]!="1":
            count+=1
    else:
        if k[j]=="1":
            count+=1
    h+=1
print(count)
    
